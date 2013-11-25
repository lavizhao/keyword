#coding: utf-8
'''
只匹配字符串，完全不搞别的
'''
import sys
import csv
import math
from operator import itemgetter

def ana(keyword):
    """
    
    Arguments:
    - `keyword`:
    """
    total_passage = 6034195
    print "标签文件：",keyword
    keyword = open(keyword)
    keyword_data = keyword.readlines()
    keyword = {}
    for key_word in keyword_data:
        sp = key_word.split()
        val = int(sp[1])
        word = sp[0]
        keyword[word] = val
    print "总标签：",len(keyword)
    kt = sorted(keyword.iteritems(), key=itemgetter(1), reverse=True)

    #topn(kt,10000)
    return keyword,kt



def count(line,words):
    """
    
    Arguments:
    - `line`:
    """
    rwords = words.replace("-","_")
    words = words.split("-")
    words.append(rwords)
    result = 1
    sp = line.split()
    for word in words:
        if line.count(word) == 0:
            result -= 5 
            break
        else:
            result += math.log(line.count(word)*len(word)) + 12.0*(len(word)-1.0) - math.log((line.find(word)+1.0)/len(word))
           #print result,word

    return result

def sigmoid(a):
    return 10.0/(1+math.exp(-a))    

def predict(title,line,keyword,kt):
    """
    
    Arguments:
    - `line`:
    - `kt`:
    """
    result = {}
    #tp = math.log(6034195.0)
    kt = kt[:10000]
    for (word,k) in kt:
        rword = word
        freq = count(line,rword)
        tfreq = count(title,rword)
        
        if freq+tfreq > 1.0:
            result[rword] = sigmoid(freq+tfreq) + (math.log(keyword[rword]) )

    rt = sorted(result.iteritems(),key=itemgetter(1),reverse=True)
    #rt = [word for (word,k) in rt]
    rt = rt[:5]
    result = []
    #for (word,k) in rt:
    #    if k>1.0:
    #        result.append(word)
    #return result        
    return rt

def output1(train_file,keyword,kt):
    """
    
    Arguments:
    - `train_file`:
    - `kt`:
    """
    print "输出文件：",test_file

    f = open(test_file)
    reader = csv.reader(f)
    topk = [word for (word,k) in kt]
    topk = topk[:100]

    a = 0

    for row in reader:
        title = row[0]
        line = row[1]
        result = predict(title,line,keyword,kt)
        print result,row[2]
        if a == 10:
            sys.exit(1)
        a += 1

def output(train_file,keyword,kt):
    """
    
    Arguments:
    - `train_file`:
    - `kt`:
    """
    print "输入文件：",test_file

    f = open(test_file)
    topk = [word for (word,k) in kt]
    topk = topk[:100]

    a = 0

    while(True):
        row = f.readline()
        if a == 0:
            a += 1
            continue
        row = row.split(';')
        line = row[0]
        title = " "
        result = predict(title,line,keyword,kt)
        print result,row[1].strip()


def usage():
    """
    """
    print '''
    这个文件是一个只是字符串匹配的，完全没有任何的显示学习的文本，只是为了涨一下姿势
    想要调用，要输入：
          python just_counting.py ../data/Test.csv ../data/keyword_freq.txt
    '''
    sys.exit(1)        
    
if __name__ == '__main__':
    if len(sys.argv) != 3:
        usage()
        
    test_file = sys.argv[1]    
    keyword = sys.argv[2]
    keyword,kt = ana(keyword)
    output1(test_file,keyword,kt)
    
