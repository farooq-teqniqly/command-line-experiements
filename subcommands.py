import argparse


def main():
    parser = argparse.ArgumentParser(description="Tool with sub-commands")

    subparsers = parser.add_subparsers(help="Sub-commands")

    subparser_1 = subparsers.add_parser("sub1")
    subparser_2 = subparsers.add_parser("sub2")

    parser.parse_args()


if __name__ == "__main__":
    main()
