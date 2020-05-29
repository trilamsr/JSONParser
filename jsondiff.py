#!/usr/bin/python
#

import os
import sys
import argparse
import bisect
import json

# Good answers will have good interface. This includes program descriptions and
# usage of a nice argument parser like argparse.
#
DESCR = ''' Given two JSON formated files, attempts to output where they are different, if at all.'''

def arg_parser():
    parser = argparse.ArgumentParser(description=DESCR)
    parser.add_argument(
        'file_lhs',
        help='The first input file')
    parser.add_argument(
        'file_rhs',
        help='The second input file')    
    return parser

def main(args):
    lhs = json.load(file(args.file_lhs))
    rhs = json.load(file(args.file_rhs))
    if len(lhs) != len(rhs):
        print ('length mismatch. LHS: %d RHS: %d' % (len(lhs), len(rhs)))
    for idx, (lhs_row, rhs_row) in enumerate(zip(lhs, rhs)):
        # print lhs_row['id'], lhs_row['id']
        if lhs_row['id'] != rhs_row['id']:
            print ("Row mismatch. IDX: %d LHS: %s RHS: %s" % (idx, lhs_row, rhs_row))
    return 0


if __name__ == '__main__':
    args = arg_parser().parse_args()
    sys.exit(main(args))