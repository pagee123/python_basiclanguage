def scope():
    global var1
    var1=1 #全域變數
    var2 =2
    print(f"var1={var1},var2={var2}")
    
var1 = 10 #全域變數
var2 = 20
scope()
print(f"var1={var1},var2={var2}")