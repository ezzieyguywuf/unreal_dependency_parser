import parser
import argparse
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
    for data in parsedData[:5]:
        url = "{}/{}/{}".format(baseUrl, data.remotePath, data.hash)
        print("Downloading: " + url)
        req = requests.get(url)
        fname = data.hash + ".pack"
        with open(fname, 'wb') as outfile:
            outfile.write(req.content)
