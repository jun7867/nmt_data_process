# _*_ coding: utf8 _*_
import argparse
import re

KO_FILE = "/hdd/data/koen-park/clean/test.ko"
EN_FILE = "/hdd/data/koen-park/clean/test.en"

OUT_KO_FILE = KO_FILE+".clean"
OUT_EN_FILE = EN_FILE+".clean"

if __name__ == '__main__':

    wf_ko = open(OUT_KO_FILE, "w")
    wf_en = open(OUT_EN_FILE, "w")
    rf_ko = open(KO_FILE, "r")
    rf_en = open(EN_FILE, "r")

    count = 0
    p_colon = re.compile(r".*[\"].*")
    p_bracket = re.compile(r"^\(.*\)")
    p_slash = re.compile(r".*/.*")
    p_starting_number = re.compile(r"^\s?[0-9]+\.[^0-9]")
    p_date = re.compile(r".*[0-9]{4}\.[0-9]{2}.*")
    p_dash = re.compile(r"^\s?-\s?")

    line_nums = []

    ko_sents = []
    en_sents = []
    filter_sents = []
    for i, (ko_line, en_line) in enumerate(zip(rf_ko.readlines(), rf_en.readlines())):
        sent_ko = ko_line.decode('utf8').rstrip().lstrip()
        sent_en = en_line.decode('utf8').rstrip().lstrip()
        sent_ko = sent_ko.replace("", "")
        sent_en = sent_en.replace("", "")

        # print(sent_ko)
        sent_ko = re.sub(r'\(.+\)', '', sent_ko)
        sent_en = re.sub(r'\(.+\)', '', sent_en)

        # sent_en = re.sub(r'(&#[0-9]+;\s+)', "", sent_en)
        # sent_ko = re.sub(r'(&#[0-9]+;\s+)', "", sent_ko)

        if sent_en[-1] == ":":
            print(i + 1), sent_en
            line_nums += [i]

        if len(sent_en) < 30:
            print(i+1), sent_en
            line_nums += [i]

        # if p_dash.match(sent_ko) is not None:
        #     print (i + 1), sent_ko
        #     sent_ko = re.sub(r"^\s?-\s?", "", sent_ko)
        #     print(sent_ko)
        #     line_nums += [i]

        # if p_bracket.match(sent_ko) is not None:
        #     print (i+1), sent_ko
        #     sent_en = re.sub(r"\(.*\)", "", sent_en)
        #     print(sent_en)

        # if p_date.match(sent_ko) is not None:
        #     print(i + 1), sent_ko
        #     if i > 1000:
        #         line_nums += [i]

        # if p_starting_number.match(sent_ko) is not None:
        #     print(i+1), sent_ko
        #     sent_ko = re.sub(r"(^\s?[0-9]+\.\s?)", "", sent_ko)
        #     print(sent_ko)
        #     # line_nums += [i]
        #
        # if p_starting_number.match(sent_en) is not None:
        #     print(i+1), sent_en
        #     sent_en = re.sub(r"(^\s?[0-9]+\.\s?)", "", sent_en)
        #     print(sent_en)

        filter_text = '(AP)'
        if '(AP)' in sent_en:
            # print (i + 1), sent_en
            start_idx = sent_en.index(filter_text)+len(filter_text)+1
            sent_en = sent_en[start_idx:]
            if sent_en[0] == '_':
                sent_en = sent_en[2:]
            print(sent_en)

        # if sent_en[0] == '_':
        #     print (i + 1), sent_en
        #     line_nums += [i]


        # if p_colon.match(sent_ko) is not None:
        #     # print (i+1), sent_ko
        #     # print (i+1), sent_en
        #     line_nums += [i]

        # if p_bracket.match(sent_ko) is not None:
        #     print (i + 1), sent_ko
        #     line_nums += [i]
        #
        # if p_colon.match(sent_en) is not None:
        #     print (i + 1), sent_en
        #     line_nums += [i]

        # if p_bracket.match(sent_en) is not None:
        #     print (i + 1), sent_en
        #     # line_nums += [i]

        # if p_slash.match(sent_ko) is not None:
        #     # print (i+1), sent_ko
        #     line_nums += [i]
        #
        # if p_slash.match(sent_en) is not None:
        #     # print (i+1), sent_en
        #     line_nums += [i]

        # if sent_en in en_sents:
        #     print (i + 1), sent_en
        #     line_nums += [i]

        # if sent_ko in ko_sents:
        #     print (i + 1), sent_ko
        #     line_nums += [i]
        # else:
        #     ko_sents += [sent_ko]
        #     en_sents += [sent_en]
        ko_sents += [sent_ko]
        en_sents += [sent_en]

    filtered_set = sorted(set(line_nums))
    print(filtered_set)
    print("total %d filtered !" % len(filtered_set))

    for i, (ko_line, en_line) in enumerate(zip(ko_sents, en_sents)):
        if i in filtered_set:
            continue

        wf_ko.write(ko_line.encode('utf8')+"\n")
        wf_en.write(en_line.encode('utf8')+"\n")

    wf_ko.close()
    wf_en.close()
    rf_ko.close()
    rf_en.close()


