#!/bin/bash
# input_file
EXT=$1
FILENM=$2


echo "learning bpe.."
# learn BPE on joint vocabulary
cat ${FILENM}.tok.${EXT} | python subword_nmt/learn_bpe.py -s 30000 > ${EXT}.bpe

echo "applying bpe.."
python subword_nmt/apply_bpe.py -c ${EXT}.bpe < ${FILENM}.tok.${EXT} > ${FILENM}.bpe.${EXT}