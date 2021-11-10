#! /usr/bin/env python
"""
Author: Frank
Purpose: Say Hello
"""

import argparse


def get_args():
    """Get the command-line arguments"""

    parser = argparse.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', metavar='name',
                        default='World', help='Name to greet')
    return parser.parse_args()


def main():
    """Main"""

    args = get_args()
    name = args.name
    print('Hello, ' + name + '!')


if __name__ == '__main__':
    main()
