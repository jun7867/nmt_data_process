import os
import re
from argparse import ArgumentParser

os.getenv('CLASSPATH')

tag_p = re.compile(r'<.*?>')

def parse_args():
    p = ArgumentParser('Constructs vocabulary file.')
    p.add_argument(
        '--input',
        type=str, metavar='FILE', required=True, help='input xml raw corpus')
    p.add_argument(
        '--output',
        type=str, metavar='lang', required=True, help='output plain text')

    args = p.parse_args()
    return args


def main():
    args = parse_args()

    samples = []
    with open(args.input, 'r') as f:
        for i, line in enumerate(f.readlines()):
            if tag_p.match(line) is not None:
                continue    # skip lines with tag
            # if len(line.strip()) == 0:
            #     continue
            samples += [line]

    with open(args.output, 'w') as f:
        f.writelines(samples)

if __name__ == '__main__':
    main()