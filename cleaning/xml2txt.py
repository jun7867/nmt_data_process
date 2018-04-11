from bs4 import BeautifulSoup
from argparse import ArgumentParser


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

    outputs = []
    with open(args.input, "r") as f:
        xmlstr = ' '.join(f.readlines())
        bs = BeautifulSoup(xmlstr, "lxml")
        segs = bs.find_all("seg")
        for seg in segs:
            outputs += [(seg.string+"\n").encode('utf8')]

    with open(args.output, "w") as f:
        f.writelines(outputs)

if __name__ == '__main__':
    main()