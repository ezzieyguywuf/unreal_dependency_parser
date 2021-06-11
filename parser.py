import argparse
import xml.etree.ElementTree as ET

# Expects a filename, which will contain the xml data. No error-handling is
# currently incorporated - so make sure it's an actual xml file
def parseFile(fname: str) -> ET:
    print("trying to parse {}".format(fname))
    return ET.parse(fname)

def parseArguments():
    parser = argparse.ArgumentParser(description='Parse Unreal Engine deps')
    parser.add_argument('dependency_file', metavar='FILE', type=str,
                        help='The xml file containing the Unreal Engine dependencies')

    return parser.parse_args()


if __name__=="__main__":
    args = parseArguments()

    print(args.dependency_file)
    tree = parseFile(args.dependency_file)
    root = tree.getroot()

    print(root.tag)
    print(root.attrib)
