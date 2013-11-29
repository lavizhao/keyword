#coding: utf-8

import os,os.path
import csv
import sys

from whoosh import index
from whoosh.fields import *
from whoosh.qparser import QueryParser
from whoosh import scoring

INDEX_DIR = "../whoosh_index"

def search():
    """
    """

    #先建schema
    print "建模式"    
    schema = Schema(content=TEXT(stored=True),tag=TEXT(stored=True))    

    #利用index.create_in 创建索引
    
    ix = index.create_in(INDEX_DIR,schema)

    searcher = ix.searcher(weighting=scoring.TF_IDF())
    print "开文件"
    f = open("../data/test.csv")

    reader = csv.reader(f)

    a = 0
    print "开始建索引"
    for row in reader:
        cont = (row[0] + row[1]).decode('utf8','ignore')
        query = QueryParser("tag",ix.schema).parse("php")
        print query
        results = searcher.search(query)
        print results
        a += 1
        sys.exit(1)
        if a%1000 == 0:
            print "%s 已完成"% a
            
    writer.commit()
if __name__ == '__main__':
    search()
