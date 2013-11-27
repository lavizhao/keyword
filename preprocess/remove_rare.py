#coding: utf-8
'''
这个文件的作用就是找到那些在train和test中过长的，或者出现次数过少的单词
'''
import csv
import sys

def long_list(line,n):
    """
    
    Arguments:
    - `line`:
    - `n`:
    """
    result = []
    for word in line:
        if len(word) > n:
            result.append(word)

    return result

def find_long(my_file):
    """
    
    Arguments:
    - `train_file`:
    """
    f = open(my_file)
    reader = csv.reader(f)

    long_words = []
    a = 0

    n = 25
    
    for row in reader:
        title = row[0].split()
        body = row[1].split()
        
        long_words.extend(long_list(title,n))
        long_words.extend(long_list(body,n))

        if a % 1000000 == 0:
            print a
        a += 1

    f.close()
    print "length long words",len(long_words)
    result = set(long_words)    
    print "set len long words",len(result)
    return result

def find_rare(my_file,n):
    """
    
    Arguments:
    - `my_file`:
    """
    f = open(my_file)
    reader = csv.reader(f)

    wd = {}
    a = 0
    result = []
    for row in reader:
        title = row[0].split()
        body = row[1].split()

        for word in title:
            wd.setdefault(word,1)
            wd[word] = wd[word] + 1
        for word in body:
            wd.setdefault(word,1)
            wd[word] = wd[word] + 1
        if a % 100000 == 0:
            print a
        a += 1
    for word in wd:
        if wd[word] <= n:
            result.append(word)
    print "rare words length :",len(set(result))
    return result

def write_file(wf,word_set):
    """
    
    Arguments:
    - `wf`:
    """
    f = open(wf,"w")
    for ws in word_set:
        for word in ws:
            f.write("%s\n"%(word))
    f.close()



def usage():
    """
    """
    print '''
    这个文件的作用就是找到那些在train和test中过长的，或者出现次数过少的单词:
         python remove_rare.py ../data/train.csv ../data/test.csv ../data/new_stopwords.txt
    '''
    sys.exit(1)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        usage()

    train_file = sys.argv[1]
    test_file = sys.argv[2]
    ns = sys.argv[3]
    
    train_long = find_long(train_file)
    test_long = find_long(test_file)
    train_rare = find_rare(train_file,20)
    test_rare = find_rare(test_file,20)

    write_file(ns,[train_long,test_long,train_rare,test_rare])
    
