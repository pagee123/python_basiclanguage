class EMP:
    salary=0
    def set_salary(self,salary):
        if(salary>40000):
            self.salary = 40000
        else:
            self.salary=salary
    def showSal(self):
        print(f"salary={self.salary}")
        
class Manager(EMP):
    bonus=0
    def set_salary(self, salary):
        if(salary>60000):
            self.salary=60000
        else:
            self.salary=salary
    def showSal(self):
        print(f"salary={self.salary+self.bonus}")
        
john=Manager()
john.set_salary(50000)
john.showSal()