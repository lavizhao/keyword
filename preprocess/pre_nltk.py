#coding: utf-8

import csv
import nltk
import sys
import re
from nltk.corpus import stopwords as sw

def stem(word):
    for suffix in ['ing', 'ly', 'ed', 'ious', 'ies', 'ive', 'es', 's', 'ment']:
        if word.endswith(suffix) and len(word) > len(suffix) + 1:
            return word[:-len(suffix)]
    return word

def poss_train(train_file,train_write,sw_file):
    """
    
    Arguments:
    - `train_file`:
    """
    a = 0
    f = open(train_file)
    reader = csv.reader(f)

    t = open(train_write,"w")

    sw = open(sw_file)
    sw = sw.readlines()
    sw = [word.strip() for word in sw]
    
    stopwords = sw
    print "停顿词表长度",len(stopwords)
    stopwords = set(stopwords)

    g = lambda x : x not in stopwords
    
    for row in reader:
        if a == 0:
            a += 1
            continue
        if a%1000 == 0:
            print a    
        a += 1
        #if a == 8:
        #    sys.exit(1)

        title = row[1].lower()
        #clean html
        body = nltk.clean_html(row[2].lower())
        
        #work tokenize
        pattern = r"([a-z])\w+"
        body = nltk.regexp_tokenize(body, pattern)
        title = nltk.regexp_tokenize(title, pattern)

        #light stem
        title = set([stem(word) for word in title])
        body = set(body)
        body = set([stem(word) for word in body])

        #remove stopwords
        body = filter(g,body)
        title = filter(g,title)

        body = ' '.join(body)
        title = ' '.join(title)
        t.write('%s , %s , %s\n'%(title,body,row[3]))

def poss_test(test_file,test_write,sw_file):
    """
    
    Arguments:
    - `train_file`:
    """
    a = 0
    f = open(test_file)
    reader = csv.reader(f)

    t = open(test_write,"w")

    sw = open(sw_file)
    sw = sw.readlines()
    sw = [word.strip() for word in sw]
    
    stopwords = sw
    print "停顿词表长度",len(stopwords)
    stopwords = set(stopwords)

    g = lambda x : x not in stopwords
    
    for row in reader:
        if a == 0:
            a += 1
            continue
        if a%1000 == 0:
            print a    
        a += 1
        #if a == 8:
        #    sys.exit(1)

        title = row[1].lower()
        #clean html
        body = nltk.clean_html(row[2].lower())
        
        #work tokenize
        pattern = r"([a-z])\w+"
        body = nltk.regexp_tokenize(body, pattern)
        title = nltk.regexp_tokenize(title, pattern)

        #light stem
        title = set([stem(word) for word in title])
        body = set(body)
        body = set([stem(word) for word in body])

        #remove stopwords
        body = filter(g,body)
        title = filter(g,title)

        body = ' '.join(body)
        title = ' '.join(title)
        t.write('%s , %s \n'%(title,body))

def usage():
    """
    """
    print '''
    这个是用nltk 的tokinize 做的预处理，请输入，训练文件+测试文件：
             python pre_nltk.py ../data/Train.csv ../data/Test.csv ../data/train.csv ../data/test.csv ../data/stopwords.txt
    '''
    sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 6:
        usage()

    train_file = sys.argv[1]
    train_write = sys.argv[3]
    
    test_file = sys.argv[2]
    test_write = sys.argv[4]

    sw_file = sys.argv[5]
    
    print "训练文件",train_file
    print "测试文件",test_file
    print "写入训练文件",train_write
    print "写入测试文件",test_write
    print "停顿词表文件",sw_file

    poss_train(train_file,train_write,sw_file)
    poss_test(test_file,test_write,sw_file)
