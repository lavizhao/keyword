#coding: utf-8

import lucene
import csv

print "预处理"
INDEX_DIR = '../index'

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

def build_index():
    """
    """
    print "开始创建索引"
    writer = lucene.IndexWriter(directory,analyzer,True,
                                lucene.IndexWriter.MaxFieldLength.UNLIMITED)

    data = get_data()
    print "数据个数:",len(data)

    a = 0
    for content,tag in data:
        doc = lucene.Document()
        doc.add(lucene.Field('content',content,lucene.Field.Store.YES,
                             lucene.Field.Index.ANALYZED))
        doc.add(lucene.Field('tag',tag,lucene.Field.Store.YES,
                             lucene.Field.Index.NOT_ANALYZED))
        writer.addDocument(doc)
        if a % 10000 == 0:
            print "%s已完成"%(1.0*a/len(data))
        a += 1

    print "写引擎优化"
    writer.optimize()
    writer.close()

    
    
    
if __name__ == '__main__':
    print "hello world"
    build_index()


