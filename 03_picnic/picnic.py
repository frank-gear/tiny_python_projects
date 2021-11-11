#!/usr/bin/env python3
"""
Author : frank <frank@localhost>
Date   : 2021-11-10
Purpose: correctly format the items we're taking on our picnic
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='correctly format the items were taking on our picnic',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('items',
                        metavar='str',
                        nargs='+',
                        help='Items brought')

    parser.add_argument('-s',
                        '--sorted',
                        help='sort items',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """list items"""

    args = get_args()
    if args.sorted:
        args.items.sort()
    if len(args.items) > 1:
        items_arg = args.items[0:]

        if len(items_arg) == 2:
            print(f'You are bringing {items_arg[0]} and {items_arg[1]}.')
        else:
            count = len(items_arg)
            i = 1
            sent = f"You are bringing {items_arg[0]}"
            while i < (count - 1):
                item = f", {items_arg[i]}"
                i += 1
                sent = sent + item

            print(f'{sent}, and {items_arg[-1]}.')

    else:
        items = args.items[0]
        print(f'You are bringing {items}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
