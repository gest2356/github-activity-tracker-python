from get_activity import get_activity
import argparse


def main():
    parser = argparse.ArgumentParser(prog='github-tracker', description='Github Tracker')

    subparsers = parser.add_subparsers(dest='description', help='sub-command help')

    search_parser = subparsers.add_parser('search', help='search github')
    search_parser.add_argument('username', help='search query')

    args = parser.parse_args()

    if args.description == 'search':
        get_activity(args.username)

if __name__ == "__main__":
    main()