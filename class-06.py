#! /usr/bin/python
#coding=utf-8

class Student():
    Sno="" #public 
    Sname="" #public
    Age = 18
    __Money = 100 #private

    def Iam(self):
        print("I am " + self.Sno + ":" +self.Sname + " 3Q!")
        print("I hava " + str(self.__Money)+" dollors")
    
    def setMoney(self,money):
        self.__Money = money
    
    def getMoney(self):
        return(self.__Money)

st = Student()
st.Sno = "1001"
st.Sno = "JOHN"
st.setMoney(1000)
print("money=" + str(st.getMoney()))
st.Iam()
