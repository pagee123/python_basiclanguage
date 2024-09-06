#input 0 output 0
def test():
    print(".............")

#input 2 output 1 
def mul(x,y):
    return x*y

def add(x,y):
    return x+y

def minus(x,y):
    return x-y

def div(x,y):
    return x/y

#input 2 output 4
def operation1(x,y):
    mul = x*y
    add = x+y
    minus = x-y
    div = x/y
    return [mul,add,minus,div]

#input 2 output 4
def operation2(x,y):
    mul = x*y
    add = x+y
    minus = x-y
    div = x/y
    return mul,add,minus,div
############################
test()

num1=mul(2,3)
print(f"mul:{num1}")
num2=add(2,3)
print(f"add:{num2}")
num3=minus(2,3)
print(f"minus:{num3}")
num4=div(2,3)
print(f"div:{num4}")

print(".................")
result = operation1(2,3)
print(result)
for value in result:
    print(value)
    
print(".................")
res_mul,res_add,res_minus,res_div = operation2(2,3)
print(f"result:{res_mul}")
print(f"result:{res_add}")
print(f"result:{res_minus}")
print(f"result:{res_div}")