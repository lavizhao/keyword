#coding: utf-8
import sys

def morethan(keyword,n):
    """
    
    Arguments:
    - `keyword`:
    - `n`:
    """
    ans = 0
    for line in keyword:
        if len(line.split()) - 1 <= n :
            ans += 1
    print "少余%s的词占总的百分比为%s"%(n,1.0*ans/len(keyword))

def aw(kf,nc):
    """
    """
    f = open(kf)
    print kf

    keyword = f.readlines()
    print "总关键词长度：",len(keyword)

    morethan(keyword,1000)
    morethan(keyword,100)
    morethan(keyword,10)
    morethan(keyword,5)
    morethan(keyword,2)

    twf = open(nc,"w")
    a = 0
    for line in keyword:
        if len(line.split()) - 1 <= 200 :
            twf.write(line)
            a += 1
            
    print "处理后词表长度",a
    twf.close()
    

def usage():
    """
    """
    print '''
    计数文件：
      python ana_words.py ../data/counting.txt ../data/new_counting.txt
    '''
    sys.exit(1)
    
if __name__ == '__main__':
    if len(sys.argv)!= 3:
        usage()

    kf = sys.argv[1]
    nc = sys.argv[2]    
    #analysis words
    aw(kf,nc)
