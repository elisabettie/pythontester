#coding: utf-8
#--- uppgift 7---
class Product(object):
	price = 0
	count = 0
	tax = 1

	def __init__(self,price,count,tax):
		self.price = price
		self.count = count
		self.tax = tax

	def price_with_tax(self):
		return self.price * self.count * self.tax

products = [Product(price=900, count=2, tax=1.25), Product(price=100, count=1, tax=1.06)]

total_price = products[0].price_with_tax() + products[1].price_with_tax()

print total_price

#--- uppgift 6---
#class Product(object):
#	price = 0
#	count = 0
#	tax = 1
#
#	def __init__(self,price,count,tax):
#		self.price = price
#		self.count = count
#		self.tax = tax
#
#	def price_with_tax(self):
#		return self.price * self.count * self.tax
#
#robot = Product(price=900, count=2, tax=1.25)
#
#book = Product(price=100, count=1, tax=1.06)
#
#print robot.price_with_tax() + book.price_with_tax()

#---uppgift 5---
#class Product(object):
#	price = 0
#	count = 0
#	tax = 1
#
#	def price_with_tax(self):
#		return self.price * self.count * self.tax
#
#robot = Product()
#robot.price = 900
#robot.count = 2
#robot.tax = 1.25
#
#book = Product()
#book.price = 100
#book.count = 1
#book.tax = 1.06
#
#print robot.price_with_tax() + book.price_with_tax()

#--- uppgift 4 ---
#class Product(object):
#	price = 0
#	count = 0
#	tax = 1

#robot = Product()
#robot.price = 900
#robot.count = 2
#robot.tax = 1.25

#book = Product()
#book.price = 900
#book.count = 1
#book.tax = 1.06

#print robot.price * robot.count * robot.tax + book.price * book.count * book.tax


#--- uppgift 3 ---
#robot = {"price":900, "count":2, "tax":1.25}
#book = {"price":100, "count":1, "tax":1.06}


#print robot["price"] * robot["count"] * robot["tax"] + book["price"] * book["count"] * book["tax"]

#---Här är en lista---
#customer_id[10,20,30]
#print customer_id[0]

#customer_namebase["bob","anna","lisa"]
#customer_namebase["anna"]

#---uppgift 2---
#robot_price = 900
#robot_count = 2
#robot_tax = 1.25

#book_price = 100
#book_count = 1
#book_tax = 1.06
#print robot_price * robot_count * robot_tax + book_price * book_count * book_tax 