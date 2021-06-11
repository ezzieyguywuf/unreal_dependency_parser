import helper
import argparse

def parseArguments():
    parser = argparse.ArgumentParser(description='Parse Unreal Engine deps')
    parser.add_argument('dependency_file', metavar='FILE', type=str,
                        help='The xml file containing the Unreal Engine dependencies')

    return parser.parse_args()


if __name__=="__main__":
    args = parseArguments()

    print(args.dependency_file)
    tree = helper.parseFile(args.dependency_file)
    root = tree.getroot()

    print(root.tag)
    print(root.attrib)
