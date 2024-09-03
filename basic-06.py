print("......1.........")
list_data = ('bacd',786,2.23,False,70.2)
tinylist = (123,'john')
print(list_data)
print(list_data[0])
print(list_data[1:3])
print(list_data[2:])
print(list_data*2)
print(list_data+tinylist)

#list_data[1] = "abc" #false
#走訪
#()tuple 元組 無法更改
print("get element..........")
print(list_data[2])
print("get elements........")
for e in list_data:
    print(e)
print(type(list_data))