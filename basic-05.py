#[]動態陣列 可修改

print("......1.........")
list_data = ['bacd',786,2.23,False,70.2]
tinylist = [123,'john']
print(list_data)
print(list_data[0])
print(list_data[1:3])
print(list_data[2:])
print(list_data*2)
print(list_data+tinylist)

##############################
print("update......")
list_data[2] = 'aaa'
print(list_data)
print("delete...........")
del list_data[1]
print(list_data)
print("append..........")
list_data.append('dddddd')
print(list_data)
print("insert...........")
list_data.insert(2,'eeee')
print(list_data)

#走訪
print("get elements.........")
print(list_data[2])
for e in list_data:
    print(e)

print("length........")
print(len(list_data))

print("count...........")
newlist = [1,50,50,23,50]
print(newlist.count(50))