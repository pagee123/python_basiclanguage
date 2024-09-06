#! /usr/bin/python
#coding=utf-8

class ShadowingTest:
	x=10
	y=50
	def printInfo(self,x):
		print("區域變數"+str(x))
		print("屬性"+str(self.x))
		print("屬性"+str(self.y))
		return ("x="+str(x+50))

S = ShadowingTest()
print(S.printInfo(40))