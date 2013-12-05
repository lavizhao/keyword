#coding: utf-8

if __name__ == '__main__':
    st = "data/mult/result"
    print st

    t = open("data/resultX.csv","w")
    t.write("Id,Tags\n")

    a = 0
    for i in range(21):
        print i
        f = open(st+str(i)+".csv")
        h = f.readlines()
        temp = 0
        print len(h)
        for line in h:
            t.write(line)
            a += 1
            temp += 1
        print "temp",temp
    print "total",a 
        
