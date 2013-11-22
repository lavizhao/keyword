#coding: utf-8

'''
合并两个词表
'''

if __name__ == '__main__':
    f = open("../data/new_stopwords.txt")
    g = open("../data/stopwords.txt")

    words = f.readlines()
    words1 = g.readlines()

    words = [word.strip() for word in words]
    words1 = [word.strip() for word in words1]

    g.close()
    f.close()

    g = open("../data/stopwords.txt","w")

    print len(words),len(words1)

    words.extend(words1)

    for word in words:
        g.write("%s\n"%(word))
