import argparse
import parser
import processor
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
    for pack in parsedData:
        url = "{}/{}/{}".format(baseUrl, pack.remotePath, pack.hash)
        print("Downloading: " + url)
        req = requests.get(url)

        processor.processPack(pack, req)
