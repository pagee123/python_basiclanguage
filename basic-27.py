def sell(**price):
    print(f"price={price}")
    
sell(apple=10,ball=15,cat=25)

data = {"args3":3,"args2":"two"}
#sell(data)#error
sell(**data)