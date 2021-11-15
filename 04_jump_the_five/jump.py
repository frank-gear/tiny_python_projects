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
    pos_arg = args.number

    code = {
        "1": '9',
        '2': '8',
        '3': '7',
        '4': '6',
        '5': '0',
        '6': '4',
        '7': '3',
        '8': '2',
        '9': '1',
        '0': '5'
    }

    i = 0
    num = len(pos_arg)
    nunum = ""
    while i < num:
        if pos_arg[i] in code:
            nunum = nunum + str(code.get(pos_arg[i]))
            i += 1
        else:
            nunum = nunum + str(pos_arg[i])
            i += 1
    print(nunum)


# --------------------------------------------------
if __name__ == '__main__':
    main()
