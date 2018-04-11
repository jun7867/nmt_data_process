from argparse import ArgumentParser
from collections import Counter
import csv

def parse_args():
    p = ArgumentParser("calculate distribution of maximum sequence lengths")
    p.add_argument("--input",
                   type=str, metavar='FILE', required=True, help="input corpus file")
    p.add_argument("--output",
                   type=str, metavar='FILE', required=False, help="output csv file for excel chart")


    args = p.parse_args()
    return args

def main():
    args = parse_args()

    ct = Counter()
    with open(args.input, "r") as f:
        for line in f.readlines():
            bucket = len(line.strip().split(' ')) / 10 + 1
            ct[bucket] += 1

    for bucket, count in sorted(ct.items()):
        print("~%d words: %d" % (bucket*10, count))

    if args.output is not None:
        with open(args.output, "w") as wf:
            csv_writer = csv.writer(wf, delimiter=',')
            for bucket, count in sorted(ct.items()):
                csv_writer.writerow((("len-%d" % (bucket * 10)), count))
        print("Results written to csv file.. %s" % args.output)

if __name__ == '__main__':
    main()