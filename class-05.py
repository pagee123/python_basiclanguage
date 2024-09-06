#! /usr/bin/python
#coding=utf-8

class Student():
    Sno="" #public 
    Sname="" #public
    Age = 18
    __Money = 100 #private

    def Iam(self):
        print("I am " + self.Sno + ":" +self.Sname + " 3Q!")
        self.__Money = 120
        print("I hava " + str(self.__Money)+" dollors")

st = Student()
st.Sno = "1001"
st.Sno = "JOHN"
st.Iam()
