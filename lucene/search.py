#coding: utf-8

import lucene
import csv
import sys 

print "预处理"
INDEX_DIR = '../index/'

lucene.initVM()
directory = lucene.SimpleFSDirectory(lucene.File(INDEX_DIR))
analyzer = lucene.StandardAnalyzer(lucene.Version.LUCENE_CURRENT)


def get_data():
    """
    """
    f = open("../data/new_train.csv")
    reader = csv.reader(f)

    data = []
    
    for row in reader:
        data.append((row[0]+" "+row[1],row[2]))

    return data


def search(q):
    """
    
    Arguments:
    - `q`:
    """
    #print "查询字符串 %s."%(q)

    #print "创建查询器"
    searcher = lucene.IndexSearcher(directory,True)

    query = lucene.QueryParser(lucene.Version.LUCENE_CURRENT,
                               'content',analyzer).parse(q)

    #print "查询"
    results = searcher.search(query,None,1)
    
    score_docs = results.scoreDocs

    a = 0
    for score_doc in score_docs:
        doc = searcher.doc(score_doc.doc)
        #print a,doc['content']
        a += 1
    result = doc['tag']
    searcher.close()    
    return result
    
def predict(f,label):
    """
    """
    a = 0
    reader = csv.reader(f)

    t = open("../data/result_lucene_fuck.csv","w")
    t.write("Id,Tags\n")

    searcher = lucene.IndexSearcher(directory,True)
    
    for row in reader :
        content = row[0]+" "+row[1]
        #print "查询字符串:",content
        #print "结果：",label[a],search(content)

        query = lucene.QueryParser(lucene.Version.LUCENE_CURRENT,
                                   'content',analyzer).parse(content)

        results = searcher.search(query,None,1)
    
        score_docs = results.scoreDocs

        b = 0
        for score_doc in score_docs:
            doc = searcher.doc(score_doc.doc)
            b += 1

        result = doc['tag']
        
        t.write("%s,\"%s\"\n"%(label[a],result.strip()))
        a += 1
        if a % 10 == 0:
            print "完成%s,百分之%s已经完成"%(a,1.0*a/20000.0)
        
        
if __name__ == '__main__':
    f = open("../data/test.csv")
    g = open("../data/label.txt")
    label = g.readlines()
    label = [tag.strip() for tag in label]
    label = label[1:]

    predict(f,label)
 


