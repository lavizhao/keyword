# coding: utf-8
'''
这个是处理抽样出来的文本预处理程序，规则什么的我还没有想好，慢慢想
'''

import csv
import sys
import re

def stem(body,stopwords):
    """
    这里要定几条规则：
       1. 全部转化为小写
       2. 去掉所有'\n'
       3. 
    Arguments:
    - `body`:将要处理的字符串
    """

    body = body.lower()
    body = body.strip()
    body = body.replace('\n',' ')
    body = body.replace('\t',' ')
    body = body.replace('<p>',' ')
    body = body.replace('<pre>',' ')
    body = body.replace('</pre>',' ')
    body = body.replace('< pre>',' ')
    body = body.replace('<code>',' ')
    body = body.replace('</code>',' ')
    body = body.replace('</p>',' ')
    body = body.replace('<ol>',' ')
    body = body.replace('<li>',' ')
    body = body.replace('</ol>',' ')
    body = body.replace('</li>',' ')
    body = body.replace('<a',' ')
    body = body.replace('&amp',' ')
    body = body.replace('&lt',' ')
    body = body.replace('&gt',' ')
    body = body.replace('e.g.',' ')
    body = body.replace('/',' ')
    body = body.replace('=',' ')
    body = body.replace(',',' ')
    body = body.replace('(',' ')
    body = body.replace(')',' ')
    body = body.replace('?',' ')
    body = body.replace('[',' ')
    body = body.replace(']',' ')
    body = body.replace('{',' ')
    body = body.replace('}',' ')
    body = body.replace('~',' ')
    body = body.replace(':',' ')
    body = body.replace('$',' ')
    body = body.replace('"',' ')
    body = body.replace(';',' ')
    body = body.replace('*',' ')
    body = body.replace('+',' ')
    body = body.replace('>',' ')
    body = body.replace('<',' ')
    body = body.replace('%',' ')
    body = body.replace('@',' ')
    body = body.replace('!',' ')    
    body = re.sub("\.{1,3}"," ",body)
    body = re.sub("\d+|\d.\d+", " ", body)
    body = re.sub(" +", " ", body)
    body = body.split()

    #这两个函数的作用是去掉所有以‘ 开头或者结尾的，我觉得’出现在这里肯定是多余的
    g1 = lambda x : x[1:] if x.startswith("'")  else x 
    g2 = lambda x : x[:-1] if x.endswith("'") else x

    #将所有的下划线替换成-
    g3 = lambda x : '-' if x == '_' else x
    g4 = lambda x : x if x not in stopwords else ""
    
    body = map(g1,body)
    body = map(g2,body)
    body = set(body)
    body = filter(g4,body)
    body = ' '.join(body)
    body = map(g3,body)
    body = ''.join(body)
    return body

def preposs(filename,sw_name):
    """
    
    Arguments:
    - `filename`:
    """
    #开一下停顿词表
    sf = open(sw_name)
    stopwords = sf.readlines()
    stopwords = [i.strip() for i in stopwords]
    stopwords = set(stopwords)
    #print stopwords
    
    f = open(filename)
    reader = csv.reader(f)

    content = ""

    a = 0
    end = 1000
    for row in reader:
        #print 20*'-'
        if len(row) != 4 or a >= end:
            break
        row[2] = stem(row[2],stopwords)
        #print row[2]
        #print "tags:==>",row[3]
        a += 1
        content = content + " "+row[2] 
    return content

def usage():
    """
    """
    print '''
    该程序有一个参数，你需要在python pre_sub.py后面加入文件名 加上停顿词表名
    例如：
       python pre_sub.py data/sub_train.csv data/stopwords.txt
    '''
    
if __name__ == '__main__':

    if len(sys.argv)!=3:
        usage()
        sys.exit(2)

    print 30*'='
    train_file = sys.argv[1]
    sw_name = sys.argv[2]
    print "将要预处理文件%s"%(train_file)
    
    preposs(train_file,sw_name)
    
    print 30*'='

