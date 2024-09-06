#! /usr/bin/python
#coding=utf-8

__metaclass__ = type
class Father:
	x = 50
	def printInfo(self):
		print(".....1.....")

class Child(Father):
	x = 100
	def printInfo(self):
		super(Child, self).printInfo()
		print("父x="+str(Father.x))
		print("子x="+str(self.x))
		

C = Child()
C.printInfo()
