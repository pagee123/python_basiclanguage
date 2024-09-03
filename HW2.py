height = input("請輸入身高(cm):")
weight = input("請輸入體重(kg):")
BMI = float(weight)/((float(height)/100)**2)

if BMI>=35 :
    print(f"BMI值為{BMI},屬重度肥胖")
elif BMI>=30 :
    print(f"BMI值為{BMI},屬中度肥胖")
elif BMI>=27 :
    print(f"BMI值為{BMI},屬輕度肥胖")
elif BMI>=24 :
    print(f"BMI值為{BMI},屬稍重")
elif BMI>=18.6 :
    print(f"BMI值為{BMI},屬正常範圍")
else :
    print(f"BMI值為{BMI},屬體重過輕")
