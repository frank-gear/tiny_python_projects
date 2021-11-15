#!/usr/bin/env python3
"""
Author : frank <frank@localhost>
Date   : 2021-11-11
Purpose: number changer
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='number changer',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('number',
                        metavar='str',
                        help='A positional argument')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    pos_arg = args.positional

    print(f'positional = "{pos_arg}"')

    numbers = {
        "1" : '9',
        '2' : '8',
        '3' : '7',
        '4' : '6',
        '5' : '0',
        '6' : '4',
        '7' : '3',
        '8' : '2',
        '9' : '1',
        '0' : '5'
    }

# --------------------------------------------------
if __name__ == '__main__':
    main()
