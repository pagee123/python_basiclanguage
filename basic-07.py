#建立
#{}字典
dict1 = {'name':'John','code':6734,'dept':'sales'}
print("建立.......")
print(dict1)
print(type(dict1))

#add
print("add..........")
dict1['one']="this is one"
print(dict1)
dict2={}
dict2['one']='one'
dict2[2]="two"
print(dict2)

#get element
print("get element...........")
print(dict1['code'])
print(dict2[2])
# print(dict2['sample']) #error
print(dict2.get('example'))
print(dict2.get('code'))

#update
print("update..........")
dict1['name'] = 'mary'
print(dict1)

#delete
print("delete............")
del dict1['code']
print(dict1)

#走訪
print("走訪1.....................")
for key in dict1:
    print(f"{key}->{dict1[key]}")

print("走訪2.....................")
for key,value in dict1.items():
    print(f"{key}->{dict1[key]}")

print("走訪3.....................")
for item in dict1.items():
    print(f"key:{item[0]},value:{item[1]}")
    # print(f"value:{item[1]}")

print("other...............")
dict1.clear()
print(dict1)
print(dict2.keys())
print(dict2.values())
print(type(dict2.values()))