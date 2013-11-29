#coding: utf-8

import xapian
import csv

INDEX_DIR = "../xapian"

def build_index():
    """
    """
    database = xapian.WritableDatabase(INDEX_DIR,xapian.DB_CREATE_OR_OPEN)

    indexer = xapian.TermGenerator()
    stemmer = xapian.Stem("english")

    indexer.set_stemmer(stemmer)

    f = open("../data/new_train")

    a = 0
    for row in reader:
        doc = xapian.Document()
        
    

if __name__ == '__main__':
    build_index()
