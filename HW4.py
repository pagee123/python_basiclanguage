counter = 0
sum = 0
while True:
    temp = input("請輸入捐款金額(如要結束甫算請按0): ")
    counter = int(counter)+1
    sum = sum+int(temp)
    if temp == '0':
        print(f"總捐款金額合計:{sum}")
    else :
        print(f"存入{counter}次款項,累計{sum}元") 