#!/usr/bin/env python3

import sys
import re
from argparse import ArgumentParser
from collections import defaultdict


def parse_args():
    p = ArgumentParser('Constructs vocabulary file.')
    p.add_argument(
        '--input',
        type=str, metavar='FILE', required=True, help='input stanford parse result')
    p.add_argument(
        '--output',
        type=str, metavar='FILE', required=True, help='linearized parse result')
    args = p.parse_args()
    return args


def main():
    args = parse_args()

    with open(args.input, 'r') as f:
        content = f.read()

    content_new = re.sub(r'\n{2}', '@@', content, flags=re.M)
    content_new = re.sub(r'[)]+', '', content_new, flags=re.M)
    content_new = re.sub(r'\(([^)\s]+)', r'[\1]', content_new, flags=re.M)
    content_new = re.sub(r'([\s]+)', ' ', content_new, flags=re.M)
    content_new = re.sub(r'@@', '\n', content_new, flags=re.M)
    content_new = re.sub(r'\n{2}', '\n', content_new, flags=re.M)

    # content_new = re.sub(r'( , ,)', ' ,', content_new, flags=re.M)
    # content_new = re.sub(r'( \. \.)', ' .', content_new, flags=re.M)
    # content_new = re.sub(r'( \'\')', ' \'', content_new, flags=re.M)
    # content_new = re.sub(r'( \' \')', ' &quot;', content_new, flags=re.M)
    # content_new = re.sub(r'( ``)', ' `;', content_new, flags=re.M)
    # content_new = re.sub(r'( \. \?)', ' ?', content_new, flags=re.M)
    # content_new = re.sub(r'( \: \:)', ' :', content_new, flags=re.M)
    # print(content_new)

    with open(args.output, 'w') as f:
        f.write(content_new)

if __name__ == '__main__':
    main()
