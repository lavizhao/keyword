#coding: utf-8
'''
这个文件的作用是编码，给关键词编码，给词表编码，关键词存储的文件是keyword_freq.txt,由于实际分析中，只取出现频度大于100的，其他的当作噪声处理了。
'''
import sys

def coding_keyword(kf,wkf):
    """
    """
    f = open(kf)
    keyword = f.readlines()
    print "关键词大小",len(keyword)
    keyword = [word.strip() for word in keyword]
    kw = {}
    for wc in keyword:
        sp = wc.split()
        word = sp[0]
        count = int(sp[1])
        if count>100:
            kw[word] = count
    print "筛选过后关键词大小",len(kw)
    a = 0
    t = open(wkf,"w")
    for word in kw:
        t.write("%s %s\n"%(word,a))
        a += 1

def coding_vocab(vf,wvf):
    """
    
    Arguments:
    - `vf`:
    - `wvf`:
    """
    f = open(vf)
    words = f.readlines()
    print "关键词大小",len(words)
    words = [word.strip() for word in words]

    a = 0
    t = open(wvf,"w")
    for word in words:
        t.write("%s %s\n"%(word,a))
        a += 1


        

def usage():
    """
    """
    print '''
    给关键词和词表编码
        python coding.py ../data/keyword_freq.txt ../data/test_vocab.txt ../data/coding_keyword.txt ../data/coding_vocab.txt
    '''
    sys.exit(1)
    
if __name__ == '__main__':
    if len(sys.argv) != 5:
        usage()

    kf = sys.argv[1]
    vf = sys.argv[2]
    wkf = sys.argv[3]
    wvf = sys.argv[4]

    print "关键词文件",kf
    print "词表文件",vf
    print "写入关键词文件",wkf
    print "写入词表文件",wvf

    coding_keyword(kf,wkf)
    coding_vocab(vf,wvf)
