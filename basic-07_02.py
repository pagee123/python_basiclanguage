dict1 = {"mary":85,"bill":93,"nantasha":100}
name = input("請輸入學生姓名: ")
if name in dict1:
    print(f"{name}的成績為 {dict1[name]}")
else:
    print("無此學生")
    score = int(input("輸入學生成績"))
    dict1[name]=score

print(f"content:{dict1}")