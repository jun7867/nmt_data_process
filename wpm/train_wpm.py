# _*_ coding: utf8 _*_
KO_FILE = "/hdd/data/koen-park/clean/train.ko"
import re
from collections import Counter

N = 5  # Maximum 5-gram

def combine_sent(sent):
    possible_pairs = []
    tokens = sent.split(' ')
    for i in range(len(tokens)-1):
        combined_tok = combine_token(tokens[i], tokens[i + 1])
        if combined_tok is not None:
            possible_pairs += [combined_tok]
    return possible_pairs


def combine_token(left_tok, right_tok):
    if left_tok[len(left_tok) - 1] == '_':
        return None
    if right_tok[0] == '_':
        return None
    return left_tok + right_tok

def generate_corpus_ngrams(text_lines):
    ngram_count = Counter()
    for ngram in range(2, N+1):
        count = 0
        for sent in text_lines:
            sent_tokens = sent.split(' ')
            sent_ngrams = make_sent_ngram(sent_tokens, ngram)
            for token in sent_ngrams:
                ngram_count[token] += 1
            count += len(sent_ngrams)

        print("ngram: %d - count: %d" % (ngram, count))
    return ngram_count

def is_possible_ngram(ngram_tokens):
    for i in range(len(ngram_tokens)):
        if i != len(ngram_tokens) - 1 and ngram_tokens[i][-1] == '_':
            return False
        elif i != 0 and ngram_tokens[i][0] == '_':
            return False
    return True

def make_sent_ngram(sent_tokens, ngram):
    possible_ngrams = []
    for i in range(len(sent_tokens) - ngram + 1):
        ngram_tokens = []
        for j in range(ngram):
            ngram_tokens += [sent_tokens[i+j]]
        if is_possible_ngram(ngram_tokens):
            possible_ngrams += [''.join(ngram_tokens)]
    return possible_ngrams

count = Counter()
text_lines = []
with open(KO_FILE, "r") as f:
    for l, line in enumerate(f.readlines()):
        sent = line.decode('utf8').rstrip()
        char_sent = re.sub(r'\s+', ' ', sent)
        char_sent = ''.join(char_sent).replace(" ", "_")

        # adding word boundary
        boundary_sent = []
        for i, unit in enumerate(char_sent):
            # starting word
            if i == 0:
                unit = '_'+unit

            # ending unit is period, so just pass
            if i == len(char_sent) - 1:
                count[unit] += 1
                boundary_sent += [unit]
                break

            # see left side unit
            if i != 0 and char_sent[i-1] == '_':
                unit = '_'+unit

            # see right side unit
            if char_sent[i+1] in ['_']:
                unit = unit+'_'

            # see ending unit
            if i == len(char_sent) - 2 and char_sent[i+1] in ['.', '!']:
                unit = unit+'_'

            if unit == '_':
                continue

            count[unit] += 1
            boundary_sent += [unit]

        text_lines += [' '.join(boundary_sent)]

        # print(''.join(boundary_sent))
        # if l == 100:
            # exit()
    # for word, freq in count.most_common():
    #     print word, freq

    # for i in range(100):
    #     print text_lines[i]
    #     for pairs in combine_sent(text_lines[i]):
    #         print pairs

ngram_count = generate_corpus_ngrams(text_lines)
# for ngram in ngram_list[-100:]:
#     print ngram

vocab = dict()
for ngram, count in ngram_count.most_common():
    if count >= 5:
        vocab[ngram] = count

print("total %d ngrams!" % len(vocab))         # 후보: 78,162
print("Done")


# permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC

