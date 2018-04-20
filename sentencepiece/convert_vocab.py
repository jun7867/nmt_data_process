#!/usr/bin/env python3

import sys
from argparse import ArgumentParser
from collections import defaultdict


def parse_args():
    p = ArgumentParser('convert sentence-piece vocabulary file.')
    p.add_argument(
        '--input',
        type=str, metavar='FILE', required=True, help='source corpus')
    p.add_argument(
        '--output',
        type=str, metavar='FILE', required=True, help='vocabulary file')
    args = p.parse_args()
    return args


def main():
    args = parse_args()

    with open(args.output, 'w') as wf:
        with open(args.input, 'r') as rf:
            for line in rf.readlines():
                wf.write(line.split('\t')[0]+'\n')


if __name__ == '__main__':
    main()
