# 10 ~ 20之間數字是否為質數

for num in range(10,21):
    #print(num)
    for i in range(2,int(num/2)+1): # 可以只判斷一半原因為反覆運算
        #1*N , 2*(N/2) , 3*(N/3) 依此類推
        if(num%i==0): #確定第一個因數
            j=num/i #計算第二個因數
            print(f"{num}等於{i}*{j:.0f}")
            break
else:
    print(f"{num}是一個質數")
        
