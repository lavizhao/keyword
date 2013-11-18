#coding: utf-8

'''
这个文件的主要作用是产生词频，将每个词的词频产生出来，然后添加到停顿词表上。
'''
import pre_sub
import sys

def usage():
    print '''
    该程序有一个参数，你需要在python pre_sub.py后面加入文件名 加上停顿词表名 加上写入文件名
    例如：
       python count_freq.py data/sub_train.csv data/stopwords.txt data/cf.txt
    '''

def count_fq(content):
    cd = {}
    content = content.split()
    for word in content:
        cd.setdefault(word,0)
        cd[word] += 1
    return cd

def write_to_file(cd,cf_name):
    """
    """
    f = open(cf_name,"w")
    for word in cd :
        f.write("%s %s\n"%(word,cd[word]))
    f.close()
            

if __name__ == '__main__':
    if len(sys.argv)!=4:
        usage()
        sys.exit(2)

    print 30*'='
    train_file = sys.argv[1]
    sw_name = sys.argv[2]
    cf_name = sys.argv[3]
    print "将要预处理文件%s"%(train_file)
    
    content = pre_sub.preposs(train_file,sw_name)

    cd = count_fq(content)

    write_to_file(cd,cf_name)
    
    print 30*'='
