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
    with open(args.input, 'r') as f:
        for line in f.readlines():
            sent = line.decode('utf8').rstrip().lstrip()
            sent = re.sub(r'\(.+\)', '', sent)
            char_sent = ' '.join(sent).replace("   ", " _ ")
            wf.write((char_sent+'\n').encode('utf8'))

        pass

    wf.close()

