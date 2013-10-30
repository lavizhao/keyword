#coding: utf-8
'''
功能主要是抽取训练集中的所有关键词，这个基本就用了一次
'''


import csv

f = open("Train.csv")
reader = csv.reader(f)

a = 0

keyword = set([])

for row in reader:
    if a == 0:
        print row
        a = a + 1
    else:
        print a
        sp = row[3].split()
        for i in sp:
            if i not in keyword:
                keyword.add(i)
        a = a + 1
t = open("keyword.txt","w")
for i in keyword:
    t.write(i+'\n')
