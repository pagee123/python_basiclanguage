print("........1..........")
#string
for letter in 'python':
    print(f"current letter:{letter}")
          
print(".........2.........")
#list
fruits = ["banana",'apple','mango']
for fruit in fruits:
    print(f"current fruit:{fruit}")

print("..........3.........")
#dict
dict1 = {"banana":20,"apple":50,"mango":80}
for name in dict1:
    print(name)

print("............4............")
for name,num in dict1.items():
    print(f"{name}數目為{num}")

#################################################
#dict to list
print("......4.......")
result=[]
for name,num in dict1.items():
    result.append(name)
    result.append(num)
print(result)

print("..........5...........")
#list內有多個dict
items = [{"name":"bill","score":30},
         {"name":"mary","score":60},
         {"name":"john","score":100}]

for item in items:
    print(f"name:{item['name']},score:{item['score']}")

print("..........6...............")
#for in (call by values, call by address)
list_data1 = [1,2,3,4,5]
for e in list_data1:
    e=e+10
print(list_data1)

print(items)
for item in items:
    item["score"]=item["score"]+10
print(items)