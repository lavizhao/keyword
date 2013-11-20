#coding: utf-8
'''
分析tag的数据分布
'''

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
    

def usage():
    """
    """
    print '''
    可以这样调用:
         python ana_tags.py ../data/keyword_freq.txt
    '''

if __name__ == '__main__':
    
    if len(sys.argv) != 2:
        usage()
        sys.exit(1)

    keyword = sys.argv[1]
    ana(keyword)
    
