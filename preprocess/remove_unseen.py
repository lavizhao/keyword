#coding: utf-8
'''
去除测试集为见过的词
'''

import csv
import sys

def get_test_vocab(test_file,test_vocab):
    f = open(test_file)

    reader = csv.reader(f)

    vocab = set([])

    a = 0

    temp_vocab = []
    
    for row in reader:
        title = row[0].split()
        body = row[1].split()
        
        if a % 10000==0:
            temp_vocab = set(temp_vocab)
            vocab = vocab.union(temp_vocab)
            temp_vocab = []
            print a , "vocab size", len(vocab)
        else:
            temp_vocab.extend(title)
            temp_vocab.extend(body)
        a += 1
        #if a == 100:
        #    print vocab
        #    sys.exit(1)

    t = open(test_vocab,"w")
    for word in vocab:
        t.write('%s\n'%(word))
    t.close()
        
def usage():
    """
    """
    print '''
    这个文件的作用是去除未见过的词
           python remove_unseen.py ../data/train.csv ../data/test.csv ../data/test_vocab.txt
    '''
    sys.exit(1)
    
if __name__ == '__main__':
    if len(sys.argv) != 4:
        usage()

    train_file = sys.argv[1]
    test_file = sys.argv[2]
    test_vocab = sys.argv[3]

    print "训练文件",train_file
    print "测试文件",test_file
    print "写入词表文件",test_vocab

    get_test_vocab(test_file,test_vocab)
