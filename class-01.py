class MyClass():
    text="ABC"
    def clear(self):
        self.text="" #像java的this.text
    
        
obj1=MyClass()
#取值
print(f"text={obj1.text}")
#設定值
obj1.text = "DEF"
print(f"text={obj1.text}")
#使用方法
obj1.clear()
print(f"text={obj1.text}")

