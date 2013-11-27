#!/bin/bash

echo "这个脚本的目的是处理rare word 然后重新组成脚本"

cd ../preprocess/

echo "将出现频率少于20次的词全部加入停顿词表中"
python remove_rare.py ../data/train.csv ../data/test.csv ../data/new_stopwords.txt

echo "合并两个停顿词表"
python hebing.py

echo "重新处理文件，分成train和test"
python pre_nltk.py ../data/Train.csv ../data/Test.csv ../data/train.csv ../data/test.csv ../data/stopwords.txt

echo "记录test的词表，移除test中未出现而train中出现的词"

python remove_unseen.py ../data/train.csv ../data/test.csv ../data/test_vocab.txt ../data/new_train.csv

echo "给关键词编码"

python coding.py ../data/keyword_freq.txt ../data/test_vocab.txt ../data/coding_keyword.txt ../data/coding_vocab.txt

echo "完成"

