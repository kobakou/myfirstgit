#coding: UTF-8
# 条件分岐 if 比較 < > <= >= == !=
# 論理演算 and or not
score = 55
if score > 50 and score <100:
	print "OK"
elif score == 100:
	print "execelent!!"
else:
	print "NG"

print "OK" if score > 60 else "hoge"

# 繰り返し loop
sales = [100, 120, 145, 80]
sum = 0
for sale in sales:
	sum += sale
	print sale
else:
	print sum

# continue, break 回数分繰り返し
for i in range(10):
	if i == 5:
		break
	print i

users = {"koba":40, "koji":30, "nao":55}
for key, value in users.iteritems():  # iteritems(), iterkeys(), itervalues()
	print "key:%s value:%s" % (key, value)

# while loop, continue , break
N = 0
while N <10:
	if N == 5:
		N += 1
		continue
	print N
	N += 1
else:
	print "end"

# 関数 def
# 配列に処理を実行するのが map
# 無名関数 lambda
def double(x):
	return x*x
a = [2,3,4]
print a
print map (double, a)
print map (lambda x:x*x*x, a)

# 会社からはgithub.comへはPushできないので注意！
