#! /usr/bin/python
#coding=utf-8

__metaclass__ = type
class Animal:
	def __init__(self, name):
		self.name = name

	def eat(self):
		print(self.name + "正在吃食物")

	def sleep(self):
		print(self.name + "正在睡覺")

class Dog(Animal):
	def __init__(self, name):
		super(Dog, self).__init__(name)

D = Dog('bill')
D.eat()
D.sleep()


