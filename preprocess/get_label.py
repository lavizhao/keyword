#coding: utf-8

import csv

if __name__ == '__main__':
    f = open("../data/Test.csv")

    t = open("../data/label.txt","w")

    reader = csv.reader(f)

    a = 0

    for row in reader:
        if a % 100000 == 0:
            print a
        a += 1
        t.write("%s\n"%(row[0]))
    t.close()
