#coding: utf-8

import sys
import csv
import math
from operator import itemgetter

def load_keyword_classify(kcf):
    """
    
    Arguments:
    - `kcf`:
    """
    f = open(kcf)
    keyword_classify = {}
    total = f.readlines()
    for line in total:
        sp = line.split()
        word = int(sp[0])
        sp = sp[1:]
        keyword_classify[word] = {}
        for kv in sp:
            spp = kv.split(':')
            class_word = int(spp[0])
            class_freq = int(spp[1])
            keyword_classify[word][class_word] = class_freq

    print "关键词类别大小",len(keyword_classify)
    return keyword_classify

def load_vocab_index(vi):
    """
    
    Arguments:
    - `vi`:
    """
    f = open(vi)
    print "获取词汇表索引"
    total = f.readlines()
    vocab_index = {}
    for line in total:
        sp = line.split()
        vocab_index[sp[0]] = int(sp[1])

    print "词汇表大小",len(vocab_index)
    f.close()        
    return vocab_index


def load_keyword_index(ki):
    """
    
    Arguments:
    - `ki`:
    """
    f = open(ki)
    total = f.readlines()
    keyword_index = {}
    for line in total:
        sp = line.split()
        keyword_index[sp[0]] = int(sp[1])

    print "关键词表大小",len(keyword_freq)
    f.close()        
    return keyword_index

def load_label(lf):
    """
    
    Arguments:
    - `lf`:
    """
    f = open(lf)
    print "获取标记文件"
    total = f.readlines()
    label = [word.strip() for word in total]
    label = label[1:]
    f.close()
    print "标记文件大小",len(label)
    return label


def load_keyword_freq(kff):
    """
    
    Arguments:
    - `kff`:
    """
    print "获取关键词先验信息"
    f = open(kff)

    total = f.readlines()
    keyword_freq = {}
    for line in total:
        sp = line.split()
        if int(sp[1]) > 100:
            keyword_freq[sp[0]] = int(sp[1])

    print "关键词表大小",len(keyword_freq)
    f.close()        
    return keyword_freq

def predict(kc,kf,label,ki,vi,tf):
    """
    
    Arguments:
    - `kc`:
    - `kf`:
    - `label`:
    - `ki`:
    - `vi`:
    """
    print "开始预测"
    print "打开测试语料",tf
    f = open(tf)

    reader = csv.reader(f)

    print "给关键词索引建立倒索引"
    #inverse keyword
    ik = {}
    for word in ki:
        indx = ki[word]
        ik[indx] = word

    print "给关键词建立集合"
    #keyword set
    ks = set(kc.keys())

    print "开始预测"
    a = 0
    for row in reader:
        if a % 1000 == 0:
            print a
        #title body
        tb = (row[0] + " " + row[1]).split()
        pre_tags(kc,kf,ki,ik,vi,tb,ks)
        a += 1
        if a == 2:
            sys.exit(1)
    
def pre_tags(kc,kf,ki,ik,vi,tb,ks):
    """
    
    Arguments:
    - `kc`:
    - `kf`:
    - `ki`:
    - `vi`:
    - `tb`:
    """
    
    ans = {}

    print tb
    print "vi mime",vi["mime"]
    print "vi mime in ks",vi["mime"] in ks
    for word in tb:
        #找到词对应的索引
        wi = vi[word]
        #如果索引在ki里面，即 wi in ks => 推出其有意义
        if wi in ks:
            #取出其每一个在keyword中存储的关键信息
            for kwi in kc[wi]:
                #给相应的关键词加上权重
                ans.setdefault(kwi,1.0/(len(kc[wi])*1.0))
                ans[kwi] += 1.0/(len(kc[wi])*1.0)
                #ans.setdefault(kwi,1)
                #ans[kwi] += 1
    #for k in kf:
    #    kfreq = kf[k]
    #    kindx = ki[k]
    #    ans.setdefault(kindx,math.log(kfreq/2000000.0))
    #    ans[kindx] += math.log(kfreq/2000000.0)
        
    rt = sorted(ans.iteritems(),key=itemgetter(1),reverse=True)
    rt = rt[:5]
    rs = [ik[indx[0]] for indx in rt]
    rs = ' '.join(rs)
    print rs

    

def usage():
    """
    """
    print '''
    nb版本的关键词抽取系统 关键词类别信息  关键词先验 测试文件 标记文件 关键词索引 词表索引
      python nb.py ../data/new_counting.txt ../data/keyword_freq.txt ../data/test.csv ../data/label.txt ../data/coding_keyword.txt ../data/coding_vocab.txt
    '''
    sys.exit(1)

if __name__ == '__main__':

    if len(sys.argv) != 7 :
        usage()

    #keyword classification info file
    kcf = sys.argv[1]
    print "关键词类别信息",kcf

    #keyword freq info
    kff = sys.argv[2]
    print "关键词先验信息",kff

    #test file
    tf = sys.argv[3]
    print "测试文件",tf

    #label file
    lf = sys.argv[4]
    print "标记文件",lf

    #keyword index
    ki = sys.argv[5]
    print "关键词索引",ki

    #vocab index
    vi = sys.argv[6]
    print "词汇表索引",vi

    keyword_freq = load_keyword_freq(kff)
    label = load_label(lf)
    keyword_index = load_keyword_index(ki)
    vocab_index = load_vocab_index(vi)
    keyword_classify = load_keyword_classify(kcf)
    predict(keyword_classify,keyword_freq,label,keyword_index,vocab_index,tf)
