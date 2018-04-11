import argparse
from konlpy.tag import Komoran

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input_file',
        type=str, metavar='FILE', required=True, help='input file name that needed morph analyze.')
    parser.add_argument(
        '--output_file',
        type=str, metavar='FILE', required=True, help='output file name of morph result')

    args = parser.parse_args()
    komoran = Komoran()

    print(args.input_file)

    wf = open(args.output_file, 'w')
    with open(args.input_file, 'r') as f:
        for line in f.readlines():
            result = ' '.join(komoran.morphs(line.strip().decode('utf8')))
            wf.write((result+'\n').encode('utf8'))
    wf.close()

