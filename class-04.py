#! /usr/bin/python
#coding=utf-8

class SmallMath:
	x=0 #屬性
	y=0 #屬性
	def __init__(self,x,y): #建構方法
		self.x=x
		self.y=y
	def add(self): #一般方法
		print("加法結果:"+str(self.x+self.y))
	def mul(self): #一般方法
		print("乘法結果:"+str(self.x*self.y))

S = SmallMath(20,30)
S.add()
S.mul()
