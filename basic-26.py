def buy(*price):
    print(f"price={price}")
    
buy(1,2,3,4)
data = ("bill",1,"tt")
buy(data) #會多加一層tuple
buy(*data)

list_data = ["bill",1,"tt"]
buy(*list_data)
buy(list_data)