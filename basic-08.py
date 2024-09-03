ch =input("清輸入國文成績: ")
math = input("請輸入數學成績: ")
eng = input("請輸入英文成績: ")
numSum = int(ch)+int(math)+int(eng)
avg = float(numSum)/3
print(f"成績總分:{numSum},平均成績:{avg}")