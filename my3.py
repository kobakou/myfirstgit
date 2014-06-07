#coding: UTF-8
# object
# class
# instance

class User(object):
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def greet(self):
		print "my name is %s and age is %d" % (self.name, self.age)

#継承
class SuperUser(User):
	def shout(self):
		print "%s is Super" % self.name

bob = User("Bob", 23)
tom = SuperUser("Tom", 30)

bob.greet()
print bob.name
tom.shout()

# module群
# https://docs.python.org/2/py-modindex.html

import math, random
from datetime import date
print math.ceil(5.2)
for i in range(5):
	print random.random()
print date.today()