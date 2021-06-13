import argparse
import gzip
import hashlib
import parser
import requests
import os
import os.path
import shutil

def parseArguments():
    parser = argparse.ArgumentParser(description='Parse Unreal Engine deps')
    parser.add_argument('dependency_file', metavar='FILE', type=str,
                        help='The xml file containing the Unreal Engine dependencies')

    return parser.parse_args()


if __name__=="__main__":
    args = parseArguments()

    print(args.dependency_file)
    tree = parser.parseFile(args.dependency_file)
    root = tree.getroot()
    baseUrl = root.attrib['BaseUrl']

    parsedData = parser.generateParsedData(root)
    for pack in parsedData[:5]:
        url = "{}/{}/{}".format(baseUrl, pack.remotePath, pack.hash)
        print("Downloading: " + url)
        req = requests.get(url)

        data = gzip.decompress(req.content)
        check_hash = hashlib.sha1(data)
        if pack.hash == check_hash.hexdigest():
            for blob in pack.blobs:
                blobData = data[blob.offset:blob.offset + blob.size]
                blobHash = hashlib.sha1(blobData)

                if blob.hash == blobHash.hexdigest():
                    for path in blob.paths:
                        dirname = os.path.dirname(path.filePath)
                        # This will create the directory if it doesn't exist
                        os.makedirs(dirname, exist_ok=True)
                        with open(path.filePath, 'wb') as outfile:
                            outfile.write(blobData)
                        print("    saved to: " + path.filePath)
                else:
                    print("    BLOB HASH DOES NOT MATCH. DOING NOTHING")
                    print("    (blob hash = {})".format(blobHash))
        else:
            print("PACK HASH DOES NOT MATCH. DOING NOTHING.")
