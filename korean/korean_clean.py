# _*_ coding: utf8 _*_
import argparse
import re

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input',
        type=str, metavar='FILE', required=True, help='input file name')
    parser.add_argument(
        '--output',
        type=str, metavar='FILE', required=True, help='output file name of result')

    args = parser.parse_args()

    wf = open(args.output, 'w')
    count = 0
    with open(args.input, 'r') as f:
        for i, line in enumerate(f.readlines()):
            sent = line.decode('utf8').rstrip().lstrip()
            sent = re.sub(r'\(.+\)', '\1', sent)
            if len(sent) < 20:
                print (i+1), sent
                count += 1
            char_sent = ' '.join(sent).replace("   ", " _ ")

        pass

    wf.close()

