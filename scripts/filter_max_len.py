#!/usr/bin/env python3

from argparse import ArgumentParser


def parse_args():
    p = ArgumentParser('Constructs vocabulary file.')
    p.add_argument(
        '--input',
        type=str, metavar='FILE', required=True, help='input stanford parse result')
    p.add_argument(
        '--src',
        type=str, metavar='lang', required=True, help='src language code')
    p.add_argument(
        '--tgt',
        type=str, metavar='ext', required=True, help='tgt language code')
    p.add_argument(
        '--max_len',
        type=int, metavar='int', required=True, help='max sentence length')

    args = p.parse_args()
    return args


def main():
    args = parse_args()

    srcf = open(args.input+"."+args.src, 'r')
    tgtf = open(args.input+"."+args.tgt, 'r')

    out_srcf = open(args.input+".filtered."+args.src, 'w')
    out_tgtf = open(args.input+".filtered."+args.tgt, 'w')

    for srcline, tgtline in zip(srcf.readlines(), tgtf.readlines()):
        if len(srcline.strip()) == 0:
            # print("skipping empty line!")
            continue
        tokens = srcline.split(" ")
        if 0 < len(tokens) < args.max_len:
            out_srcf.write(srcline)
            out_tgtf.write(tgtline)
        else:
            print("skipping sentence of length: %d" % len(tokens))

    srcf.close()
    tgtf.close()
    out_srcf.close()
    out_tgtf.close()

if __name__ == '__main__':
    main()
