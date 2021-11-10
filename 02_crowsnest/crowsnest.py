#!/usr/bin/env python3
"""
Author : frank <frank@localhost>
Date   : 2021-11-10
Purpose: announce the appearance of something to the captain
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Tell the captain you see something',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='word',
                        help='the thing we announce')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    aoran = "a"
    if args.word[0].lower() in "aeiou":
        aoran = "an"
    print("Ahoy, Captain, " + aoran + " " +
          args.word + " off the larboard bow!")


# --------------------------------------------------
if __name__ == '__main__':
    main()
