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

def remove_train(train_file,test_vocab,new_train):
    """
    
    Arguments:
    - `train_file`:
    - `test_vocab`:
    """
    train = open(train_file)
    vocab = open(test_vocab)

    vocab = vocab.readlines()
    vocab = [word.strip() for word in vocab]
    vocab = set(vocab)
    print "词表大小",len(vocab)

    reader = csv.reader(train)

    nt = open(new_train,"w")

    a = 0
    g = lambda x : x in vocab
    for row in reader:
        if a % 100000 == 0:
            print a
        a += 1
        r1,r2 = row[0].split(),row[1].split()
        title,body = [] ,[]
        for word in r1:
            if word in vocab:
                title.append(word)
                
        for word in r2:
            if word in vocab:
                body.append(word)

        #print len(r1),len(r2),"===>",len(title),len(body)
        #print r1,title
        title = ' '.join(title)
        body = ' '.join(body)
        
        nt.write("%s , %s , %s\n"%(title,body,row[2]))
        #print title,body
def get_vocab(my_file):
    """
    
    Arguments:
    - `train_file`:
    """
    f = open(my_file)
    print "训练文件",my_file

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
    print "train词表大小",len(vocab)

def usage():
    """
    """
    print '''
    这个文件的作用是去除未见过的词
           python remove_unseen.py ../data/train.csv ../data/test.csv ../data/test_vocab.txt ../data/new_train.csv
    '''
    sys.exit(1)
    
if __name__ == '__main__':
    if len(sys.argv) != 5:
        usage()

    train_file = sys.argv[1]
    test_file = sys.argv[2]
    test_vocab = sys.argv[3]
    new_train = sys.argv[4]

    print "训练文件",train_file
    print "测试文件",test_file
    print "写入词表文件",test_vocab

    #get_test_vocab(test_file,test_vocab)
    remove_train(train_file,test_vocab,new_train)
    #get_vocab(train_file)
    #get_vocab(test_file)
