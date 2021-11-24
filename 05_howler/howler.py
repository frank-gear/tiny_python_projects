#!/usr/bin/env python3
"""
Author : frank <frank@localhost>
Date   : 2021-11-17
Purpose: Change files to uppercase
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='change files to uppercase',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('howl',
                        metavar='str',
                        help='howl string')

    parser.add_argument('-a',
                        '--arg',
                        help='A named string argument',
                        metavar='str',
                        type=str,
                        default='')

    parser.add_argument('-i',
                        '--int',
                        help='A named integer argument',
                        metavar='int',
                        type=int,
                        default=0)

    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-o',
                        '--on',
                        help='A boolean flag',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make letters uppercase"""

    args = get_args()
    file_arg = args.file
    howl = args.howl

    if (os.path.isfile(howl)):
        fh = open(howl).read()
        print(fh.upper())

    else:
        print(howl.upper())


# --------------------------------------------------
if __name__ == '__main__':
    main()
