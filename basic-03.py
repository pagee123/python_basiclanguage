import math
print("1"+"..."*10)
name = "林小明"
score = 80
print(name+"的成績為"+str(score))
print(name,str(score)) # ,空格
print(name,str(score),sep='&',end=' ') # ,變成& 結束為空白
#########################
#參數格式化:%
print("\n2"+"..."*10)
print("%s的成績為%d"%(name,score))
print("PI=%f"%(math.pi))
print("PI=%10.3f"%(math.pi))
print("PI=%6d"%(math.pi))
#########################
#參數格式化:format
print("3"+"..."*10)
print("{}的成績為{}".format(name,score))
print("PI={}".format(math.pi))
#########################
#f-string
print("4"+"..."*10)
print(f"{name}的成績為{score}")