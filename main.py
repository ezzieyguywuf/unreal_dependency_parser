import argparse
import gzip
import hashlib
import parser
import requests

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
        print("    generated hash: {}".format(check_hash.hexdigest()))
        print("    hash match: {}".format(pack.hash == check_hash.hexdigest()))
        fname = pack.hash + ".data"
        with open(pack.hash, 'wb') as outfile:
            outfile.write(data)
