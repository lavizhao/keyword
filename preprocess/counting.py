#coding: utf-8


import sys
import csv

def count(kf,vf,tc,tf):
    """
    
    Arguments:
    - `kf`:
    - `vf`:
    - `tc`:
    """
    kf = open(kf)
    vf = open(vf)

    kw = kf.readlines()
    print "关键词索引大小：",len(kw)
    vb = vf.readlines()
    print "词表索引大小：",len(vb)

    keyword,vocab  = {},{}
    for line in kw:
        sp = line.split()
        word = sp[0]
        indx = int(sp[1])
        keyword[word] = indx

    for line in vb :
        sp = line.split()
        word = sp[0]
        indx = int(sp[1])

        vocab[word] = indx

    nb = {}
    f = open(tf)
    reader = csv.reader(f)
    a = 0
    for row in reader:
        if a % 1000 == 0:
            print a,len(nb)
        a += 1
        #现在先一起计数，等着有修改需要了再分别搞
        title = row[0]
        body = row[1]

        answer = row[2]
        
        #title body 
        tb = (row[0]+" "+row[1]).split()

        sp = answer.split()

        for kword in sp:
            if keyword.has_key(kword):
                indx = keyword[kword]
                for word in tb:
                    #title body index
                    tbindx = vocab[word]
                    nb.setdefault(tbindx,{})
                    nb[tbindx].setdefault(indx,1)
                    nb[tbindx][indx] += 1
    #to write file
    tfw = open(tc,"w")                
    for tbindx in nb:
        tfw.write("%s "%(tbindx))
        for indx in nb[tbindx]:
            tfw.write("%s:%s "%(indx,nb[tbindx][indx],))
        tfw.write("\n")
    tfw.close()
    

def usage():
    """
    """
    print '''
    计数文件：
      python counting.py ../data/coding_keyword.txt ../data/coding_vocab.txt ../data/counting.txt ../data/new_train.csv
    '''
    sys.exit(1)
    
if __name__ == '__main__':
    if len(sys.argv) != 5:
        usage()

    kf = sys.argv[1]
    vf = sys.argv[2]
    tc = sys.argv[3]
    tf = sys.argv[4]

    print "关键词索引:",kf
    print "词表索引:",vf
    print "写入计数文件:",tc
    print "训练文件:",tf

    count(kf,vf,tc,tf)
