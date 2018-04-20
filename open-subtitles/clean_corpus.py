# _*_ coding: utf8 _*_
import argparse
import re
import numpy as np

KO_FILE = "/hdd/data/open-subtitles2018-en-ko/OpenSubtitles2018.en-ko.ko"
EN_FILE = "/hdd/data/open-subtitles2018-en-ko/OpenSubtitles2018.en-ko.en"

OUT_KO_FILE = KO_FILE+".out"
OUT_EN_FILE = EN_FILE+".out"

if __name__ == '__main__':

    rf_ko = open(KO_FILE, "r")
    rf_en = open(EN_FILE, "r")

    line_nums = []
    ko_sents = []
    en_sents = []
    for i, (ko_line, en_line) in enumerate(zip(rf_ko.readlines(), rf_en.readlines())):
        sent_ko = ko_line.strip()
        sent_en = en_line.strip()

        sent_ko = re.sub(r"-\s", "", sent_ko)
        sent_en = re.sub(r"-\s", "", sent_en)

        sent_ko = re.sub(r"\.\.\.", "", sent_ko)
        sent_en = re.sub(r"\.\.\.", "", sent_en)

        if len(sent_ko.split(' ')) < 3:
            line_nums += [i]
            continue

        ko_sents += [sent_ko]
        en_sents += [sent_en]

    rf_ko.close()
    rf_en.close()

    # =====================

    filtered_set = sorted(set(line_nums))
    # print(filtered_set)
    print("total %d filtered !" % len(filtered_set))

    # dev, test split with 5000, 5000
    random_indexes = np.random.choice(range(len(ko_sents)), 10000, replace=False)
    half = int(len(random_indexes)/2)
    dev_indexes = random_indexes[:half]
    test_indexes = random_indexes[half:]

    print(len(ko_sents))
    print(len(en_sents))

    train_ko_sents = []
    train_en_sents = []
    dev_ko_sents = []
    dev_en_sents = []
    test_ko_sents = []
    test_en_sents = []

    for i, (ko_sent, en_sent) in enumerate(zip(ko_sents, en_sents)):
        if i in dev_indexes:
            dev_ko_sents += [ko_sent]
            dev_en_sents += [en_sent]

        elif i in test_indexes:
            test_ko_sents += [ko_sent]
            test_en_sents += [en_sent]

        else:
            train_ko_sents += [ko_sent]
            train_en_sents += [en_sent]

    print(len(train_ko_sents))
    print(len(train_en_sents))

    with open("/hdd/data/open-subtitles2018-en-ko/open-subtitles.train.ko", "w") as wf:
        wf.writelines('\n'.join(train_ko_sents)+'\n')

    with open("/hdd/data/open-subtitles2018-en-ko/open-subtitles.train.en", "w") as wf:
        wf.writelines('\n'.join(train_en_sents)+'\n')

    with open("/hdd/data/open-subtitles2018-en-ko/open-subtitles.dev.ko", "w") as wf:
        wf.writelines('\n'.join(dev_ko_sents)+'\n')
    with open("/hdd/data/open-subtitles2018-en-ko/open-subtitles.dev.en", "w") as wf:
        wf.writelines('\n'.join(dev_en_sents)+'\n')

    with open("/hdd/data/open-subtitles2018-en-ko/open-subtitles.test.ko", "w") as wf:
        wf.writelines('\n'.join(test_ko_sents)+'\n')
    with open("/hdd/data/open-subtitles2018-en-ko/open-subtitles.test.en", "w") as wf:
        wf.writelines('\n'.join(test_en_sents)+'\n')

    with open("/hdd/data/open-subtitles2018-en-ko/open-subtitles.ko", "w") as wf:
        wf.writelines('\n'.join(ko_sents)+'\n')
    with open("/hdd/data/open-subtitles2018-en-ko/open-subtitles.en", "w") as wf:
        wf.writelines('\n'.join(en_sents)+'\n')

