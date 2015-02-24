#!/usr/bin/env python3

import argparse

def main():
    # We have to specify a usage string or it'll display backwards and 
    # incorrectly
    args = argparse.ArgumentParser(
            description="Generates a latex truth table",
            usage='%(prog)s [-h] var [var ...] [-s P [P ...]]')
    args.add_argument('variables', nargs='+', metavar='var', 
                      help="Input variables to include in the truth table")
    args.add_argument('-s', '--sentences', nargs='*', metavar='P', 
                      default='X', help="Named result rows to fill with temporary values")
    inputs = args.parse_args()
    generate_table(inputs)

def generate_table(inputs):
    print(inputs)

if __name__ == '__main__':
    main()
