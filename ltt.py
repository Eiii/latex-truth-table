#!/usr/bin/env python3

import argparse
import itertools

(true_str, false_str, placeholder_str) = ("T", "F", "?")

def main():
    # We have to specify a usage string or it'll display backwards and 
    # incorrectly
    args = argparse.ArgumentParser(
            description="Generates a latex truth table",
            usage='%(prog)s [-h] var [var ...] [-s P [P ...]]')
    args.add_argument('variables', nargs='+', metavar='var',
                      help="Input variables to include in the truth table")
    args.add_argument('-r', '--results', nargs='*', metavar='P', default='X',
                      help="Named result columns to fill with temporary values")
    inputs = args.parse_args()
    generate_table(inputs)

def generate_table(inputs):
    vars = list(inputs.variables)
    results = list(inputs.results)
    num_cols = len(vars)+len(results)

    # Calculate table header/footer
    col_spec = "|{}|".format('|'.join(['c']*num_cols))
    header = r"\begin{{tabular}}{{{}}} \hline".format(col_spec)
    footer = r"\hline \end{tabular}"

    # Calculate table body
    body = list()

    # Variable names row
    name_str = ' & '.join(vars+results)
    name_str += r' \\'
    body.append(name_str)

    # Variable values rows
    for row in itertools.product((true_str, false_str), repeat=len(vars)):
        row = list(row) + [placeholder_str]*len(results)
        row_str = ' & '.join(row)+r' \\'
        body.append(row_str)
    
    # Combine and print
    print(header)
    print('\n'.join(body))
    print(footer)

if __name__ == '__main__':
    main()
