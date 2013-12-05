#coding: utf-8

import csv
import threading
import lucene

from lucene import getVMEnv

print "预处理"

INDEX_DIR = '../index/'
nt = 100000

WRITE_DIR = "../data/mult/"

lucene.initVM()
directory = lucene.SimpleFSDirectory(lucene.File(INDEX_DIR))
analyzer = lucene.StandardAnalyzer(lucene.Version.LUCENE_CURRENT)

class sub_thread(threading.Thread):
    """
    """
    
    def __init__(self, cont,lab,i):
        """
        
        Arguments:
        - `train`:
        """
        threading.Thread.__init__(self) 
        self.content = cont
        self.label = lab
        self.i = i
        print "len label",len(self.label)

    def run(self):
        owf = "%sresult%s.csv"%(WRITE_DIR,self.i)
        print owf
        
        t = open(owf,"w")

        getVMEnv().attachCurrentThread()
        searcher = lucene.IndexSearcher(directory,True)

        a = 0

        for line in self.content:
            query = lucene.QueryParser(lucene.Version.LUCENE_CURRENT,
                                       'content',analyzer).parse(line)
            results = searcher.search(query,None,1)
    
            score_docs = results.scoreDocs

            b = 0
            for score_doc in score_docs:
                doc = searcher.doc(score_doc.doc)
                b += 1

            result = doc['tag']
        
            t.write("%s,\"%s\"\n"%(self.label[a],result.strip()))
            a += 1
            if a % 10 == 0:
                print "线程%s 完成%s,百分之%s已经完成"%(self.i,a,1.0*a/len(self.content))


        
        

def div(n,length):
    """
    """
    result = []
    for i in range(length+1):
        if i % n == 0 or i == length:
            result.append(i)

    return result

def main():
    """
    """
    print "读文件"
    f = open("../data/test.csv")
    reader = csv.reader(f)

    content = []

    for row in reader:
        content.append(row[0]+" "+row[1])

    print "测试数据个数",len(content)

    turn = div(nt,len(content))

    print turn

    f.close()

    print "读标签"
    g = open("../data/label.txt")
    label = g.readlines()
    label = [word.strip() for word in label]

    label = label[1:]

    for i in range(len(turn)-1):
        sub_cont = content[turn[i] : turn[i+1] ]
        sub_label = label[turn[i] : turn[i+1]][:]
        mthread = sub_thread(sub_cont,sub_label,i)
        mthread.start()

if __name__ == '__main__':
    print "hello world"
    main()
    
