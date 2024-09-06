#! /usr/bin/python
#coding=utf-8

class Animal():#父類別

    def __init__(self, name): #建構方法 
        self.name = name #屬性，與java不同，可在此設定        
    def fly(self): #一般方法       
        print(self.name + " fly!")
        
class Bird(Animal):#子類別       
    def __init__(self, name): #建構方法，會覆寫父類別的建構方法
        self.name = "red " + name #屬性，與java不同，可在此設定        
    def sing(self): #一般方法      
        print(self.name + " sing!")        

print(".......1.......")
pigeon = Animal("pigeno")
pigeon.fly()  

print(".......2.......")      
parrot = Bird("parrot")  
parrot.fly()  
parrot.sing() 