#1+2+3+4+5
num =int(input("Enter your number:"))
count=0
i=1
while(i<=num):
    print(f"This number is:{i}")
    count = count + i
    i=i+1
print(f"the total is {count}")