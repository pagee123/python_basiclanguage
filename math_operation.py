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