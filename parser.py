import argparse

if __name__=="__main__":
    parser = argparse.ArgumentParser(description='Parse Unreal Engine deps')
    parser.add_argument('dependency_file', metavar='FILE', type=str,
                        help='The xml file containing the Unreal Engine dependencies')

    args = parser.parse_args()
    print(args.dependency_file)
