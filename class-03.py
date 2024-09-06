class TaipeiBank:
    balance=0 #屬性
    def __init__(self,balance):#建構方法
        self.balance = balance
    def printbalance(self):#一般方法
        print(f"存款餘額:{self.balance}")
        
t=TaipeiBank(200)
t.printbalance()