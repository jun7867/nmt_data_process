#  기계번역 전처리

## 1. 영어 전처리

### Normalization + Tokenization
  
(예: 영어 데이터 파일을 /nmt/data/train.en 이라고 가정함)
```
cd scripts/
```
```
./tokenize.sh en /nmt/data/train
```
train.norm.en, train.tok.en 파일이 생성되고 BPE 단계에서 train.tok.en을 사용함
   	
### Byte-pair Encoding

```
cd scripts/
```
```
./apply_bpe.sh en /nmt/data/train
```
train.bpe.en 파일이 생성되고 학습 파일로 사용

### En Vocabulary 생성

  * --input: 입력파일
  * --output: 사전파일
  * --size: 사전크기 제한 (0은 제한없음)
  
```
python make_vocab.py --input /nmt/data/train.bpe.en --output /nmt/data/vocab.en --size 30000
```

## 2. 한국어 전처리

### 음절 단위 Segmentation

```
cd korean/
```
```
python korean_char.py --input /nmt/data/train.ko --output /nmt/data/train.char.ko
```

### Normalization + Tokenization

```
cd scripts/
```
```
./tokenize.sh ko /nmt/data/train.char
```
영어 전처리 과정과 기본적으로 같지만 normalization + tokenization을 segmentation 후에 함

### Ko Vocabulary 생성

  * --input: 입력파일
  * --output: 사전파일
  * --size: 사전크기 제한 (0은 제한없음)
  
```
python make_vocab.py --input /nmt/data/train.char.tok.ko --output /nmt/data/vocab.ko --size 0
```
(한국어 음절단위는 사전크기가 크지 않기때문에 size값을 0으로 함)


## 3. Dev set 생성하는 법

train set의 첫 2000 라인을 dev set으로 분리하는 법
```
cp train.en tmp.en
head -2000 tmp.en > dev.en
tail --lines=+2001 tmp.en > train.en
```
