keyword
=======

keyword extraction for kaggle facebook keyword extraction competation

标签文件： ../data/keyword_freq.txt
总标签： 42048
TOP 5词：
('c#', 463526)
('java', 412189)
('php', 392451)
('javascript', 365623)
('android', 320622)
出现频率大于100的词共有10138个
占总的标记百分比0.957526751589
====================
出现频率大于1000的词共有2148个
占总的标记百分比0.814420901007
====================
出现频率大于10000的词共有234个
占总的标记百分比0.515311492928
====================
出现频率大于20000的词共有96个
占总的标记百分比0.405413005886
====================
平均tag长度2.88522230389

这里是数据分析的结果

如果想要得到一个好的精度，必须取到tag出现次数为100以上的词，这样在训练的时候才能有一个好的效果

我觉得对于出现频率10000-20000 的词频的tag，引用ml的方式学习，而且这样做的效果也会相对好一些
对于出现词频10000一下的词，用ML学习显然效果不会好，这些词出现的几率连万分之一都不到，肯定学不出来的。
