#coding: utf-8
'''
分析tag的数据分布
'''

import csv
import sys
from operator import itemgetter

def topn(kt,n):
    """
    
    Arguments:
    - `keyword`:
    """
    print "TOP %s词："%(n)
    for i in range(n):
        print kt[i]

def morethan(kt,n):
    """
    
    Arguments:
    - `n`:
    """
    total = 0
    temp = 0
    r = 0
    for (word,k) in kt:
        total += k
        if k > n:
            r += 1
            temp += k
    print "出现频率大于%s的词共有%s个"%(n,r)
    print "占总的标记百分比%s"%(1.0*temp/total)
    print 20*"="

def avg(kt,total_passage):
    """
    
    Arguments:
    - `kt`:
    """
    total = 0
    for (word,k) in kt:
        total += k
        
    print "平均tag长度%s"%(1.0*total/total_passage)

    
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
    topn(kt,5)

    morethan(kt,100)
    morethan(kt,1000)
    morethan(kt,10000)
    morethan(kt,20000)
    
    avg(kt,total_passage)
    
    #topn(kt,10000)
    return kt

def init_tag_per(tag_per):
    """
    
    Arguments:
    - `tag_per`:
    """
    n = 5
    for i in range(n):
        temp = [0 for j in range(i+2)]
        tag_per.append(temp)


def topwords(kt):
    """
    
    Arguments:
    - `kt`:
    """
    result = []
    limit = 20000
    for (word,k) in kt:
        if k > limit:
            result.append(word)
    return set(result)

def count_per(line,tag_per,tws):
    """
    
    Arguments:
    - `kt`:
    """
    words = line.split()
    words = [word.strip() for word in words]
    n = len(words) 
    tc = 0
    for word in words:
        if word in tws:
            tc += 1

    tag_per[n-1][tc] += 1
    

def ana_tag(train_file,kt):
    """
    
    Arguments:
    - `train_file`:
    """
    f = open(train_file)
    reader = csv.reader(f)

    tag_per = []
    init_tag_per(tag_per)

    tws = topwords(kt)

    a = 0
    for row in reader:
        if a == 0:
            a += 1
            continue
        else:
            if a % 1000000 == 0:
                print a
            a += 1
            count_per(row[3],tag_per,tws)
            
    for i in range(len(tag_per)):
        s = sum(tag_per[i])
        tag_per[i] = [1.0*e/s for e in tag_per[i]]
        print "%s tag常用tag所占百分比"%(i+1),tag_per[i]
    

    

def usage():
    """
    """
    print '''
    可以这样调用:
         python ana_tags.py ../data/keyword_freq.txt ../data/Train.csv
    '''

if __name__ == '__main__':
    
    if len(sys.argv) != 3:
        usage()
        sys.exit(1)

    keyword = sys.argv[1]
    train_file = sys.argv[2]    
    kt = ana(keyword)
    ana_tag(train_file,kt)
