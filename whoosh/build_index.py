#coding: utf-8

import os,os.path
import csv

from whoosh import index
from whoosh.fields import *

INDEX_DIR = "../whoosh_index"

def build_index():
    """
    """
    #先建一个文件夹
    print "建文件夹"
    if not os.path.exists(INDEX_DIR):
        os.mkdir(INDEX_DIR)

    #先建schema
    print "建模式"    
    schema = Schema(content=TEXT(stored=True),tag=TEXT(stored=True))    

    #利用index.create_in 创建索引
    
    ix = index.create_in(INDEX_DIR,schema)

    writer = ix.writer()
    print "开文件"
    f = open("../data/new_train.csv")

    reader = csv.reader(f)

    a = 0
    print "开始建索引"
    for row in reader:
        cont = (row[0] + row[1]).decode('utf8','ignore')
        ta = row[2].decode('utf8','ignore')
        writer.add_document(content=cont,tag=ta)
        a += 1
        if a%1000 == 0:
            print "%s 已完成"% a
            
    writer.commit()
if __name__ == '__main__':
    build_index()
