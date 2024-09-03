score=int(input("請輸入成績"))
if(score>=90):
    print("Lv A")
elif(score>=80):
    print("Lv B")
elif(score>=70):
    print("Lv C")
elif(score>=60):
    print("Lv D")
else:
    print("Lv E")

test_list=[1,2,3,4,5,6]
for e in test_list:
    if(e==4):
        print("element exists")

if(4 in test_list):
    print("element exists")