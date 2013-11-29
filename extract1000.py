#coding: utf-8
'''
抽取训练数据400条，用来实验预处理等的效果
'''

import csv

if __name__ == '__main__':
    f = open("data/new_train.csv")

    a = 0
    sample_size = 100

    train = []

    for a in range(sample_size):
        row = f.readline()
        train.append(row)
    
        

    f.close()

    t = open("data/sub_train.csv","w")
    for row in train:
        t.write(row)
