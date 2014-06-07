# coding: UTF-8
# コメント

msg = "hello world"
print msg
print 2.0**3
print u"無駄!!" * 10
print 'it\'s a pen.'

# リスト [] 変更できる, list()
# タプル () 変更できない, tuple()
# セット([]) 重複を許さない集合
# 辞書
# 文字列操作 len, find, []
# 型変換 int float str

age = 5+ int("5")
print "my age is " + str(age);

#リスト(配列)
sales = [1,4,10,8]
print len(sales)
print sales[0]
sales[0]=100
print sales[0]
print 100 in sales
print sales

# range
print range(3, 10)
print range(3, 10, 2)

# sort, reverse
sales.sort()
print sales
print tuple(sales)
# 文字列操作 split, join 
d = "2014/6/07"
print d
print "-".join(d.split("/"))

# 集合演算
a = set([1,2,3,4,53,123,53,1])
print a
b = set([1,9,5,4,53,123,53,1])
print b
print a-b
print a|b
print a&b
print a^b

# 辞書型 key, value
dic = {"koba":200,"koji":250, "shige":180,"naoki":170}
print dic
print dic["naoki"]
#print dic.items()
# in
print "naoki" in dic
print "tetsuya" in dic
print dic.keys()
print dic.values()

#表示
print "age: %03d" % age
print "koba's sales: %(koba)d" % dic
print "%f and %d" % (age, len(dic))

