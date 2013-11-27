#coding: utf-8

import sklearn
import csv
from sklearn.feature_extraction.text import HashingVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.neighbors import BallTree as BallTree
from sklearn.neighbors import NearestNeighbors

if __name__ == '__main__':
    print "建立hv"

    f = open("../data/new_train.csv")
    hv = HashingVectorizer(strip_accents='unicode',token_pattern=r'\w{1,}',decode_error='ignore',n_features = 200000)
    
    vec = TfidfVectorizer(sublinear_tf=True,min_df = 3,ngram_range=(1,2),smooth_idf=True,token_pattern=r'\w{1,}',use_idf=1,analyzer='word',strip_accents='unicode',decode_error='ignore')

    train = []
    reader = csv.reader(f)
    for row in reader:
        train.append(row[0]+" "+row[1])

    print "转化为tf-idf"
    train = train[:100000]
    x = hv.fit_transform(train)

    print "开始建树"
    nbrs = NearestNeighbors(n_neighbors=1, algorithm='ball_tree').fit(x)
    

    print x
    print x[0]



    
    
    
    
