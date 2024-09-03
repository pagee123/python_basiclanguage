select = input("要轉換(1)公尺->英尺 (2)公斤->英磅: ")
value = input("請輸入欲轉換數字: ")

if select == '1':
    res = float(value)*3.28
    print(f"{float(value)}公尺={res}英尺")
elif select == '2':
    res = float(value)*2.2
    print(f"{float(value)}公斤={res}英磅")
else:
    print("無此選項")