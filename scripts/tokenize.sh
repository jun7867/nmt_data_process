#!/bin/bash
# input_file
EXT=$1
FILENM=$2


echo "normalizing punctuation.."
perl normalize-punctuation.perl -l ${EXT} < ${FILENM}.${EXT} > ${FILENM}.norm.${EXT}

echo "tokenizing.."
perl tokenizer.perl -l ${EXT} -threads 10 < ${FILENM}.norm.${EXT} > ${FILENM}.tok.${EXT}
