#coding: utf-8

import sys
import csv
from operator import itemgetter
from matplotlib import pyplot as plt

def count_tag_freq(train_file,keyword_file,keyword_freq):
    """
    
    Arguments:
    - `train_file`:
    """
    keyword = open(keyword_file)
    keyword = keyword.readlines()
    keyword = [i.strip() for i in keyword]
    #print keyword
    keyword = {}.fromkeys(keyword,0)

    f = open(train_file)
    reader = csv.reader(f)

    a = 0
    for row in reader:
        if a == 0:
            a += 1
            continue
        line = row[3]
        sp = line.split()
        for word in sp:
            word = word.strip()
            keyword[word] += 1
        if a %10000 == 0:
            print a    
        a += 1
    #keyword_tuple = [(keyword[word],keyword) for word in keyword]
    #keyword_tuple.sort()
    keyword_tuple = sorted(keyword.iteritems(), key=itemgetter(1), reverse=True)

    vals = [i[1] for i in keyword_tuple]

    t = open(keyword_freq,"w")
    for word,k in keyword_tuple:
        t.write("%s %s\n"%(word,k))
    t.close()
    plt.plot(vals,'bo')
    plt.show()
    
        
def usage():
    """
    """
    print '''
    这个程序的作用是分析关键字的数量分布
    请输入正确的命令，用法为，训练文件+关键词文件+写入文件，例如：
          python plot_tag.py ../data/Train.csv ../data/keyword.txt ../data/keyword_freq.txt
    '''

if __name__ == '__main__':
    if len(sys.argv) != 4:
        usage()
        sys.exit(1)
        
    keyword_file = sys.argv[2]
    train_file = sys.argv[1]
    keyword_freq = sys.argv[3]

    print "关键词文件：",train_file
    print "输入文件：",keyword_file
    print "写入文件：",keyword_freq

    count_tag_freq(train_file,keyword_file,keyword_freq)

    
