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

    parser.add_argument('-o',
                        '--outfile',
                        help='A readable file',
                        metavar='str',
                        type=str,
                        default=None)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make letters uppercase"""

    args = get_args()
    file_arg = args.outfile
    howl = args.howl

    if os.path.isfile(howl):
        fhan = open(howl, 'r').read()
        if file_arg:
            file = open(file_arg, 'w')
            file.write(fhan.upper())

        else:
            print(fhan.upper())

    else:
        if file_arg:
            fhan = howl
            file = open(file_arg, 'w')
            file.write(fhan.upper())

        else:
            print(howl.upper())


# --------------------------------------------------
if __name__ == '__main__':
    main()
