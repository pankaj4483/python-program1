class employee:
    def __init__(self,name,salary):
        self.name=name
        self._salary=salary
    def get_salary(self):
        return self._salary
    def calculate_bonus(self):
        return self._salary*0.10

class manager(employee):
    def __init__(self,name,salary):
        super().__init__(name,salary)
    def calculate_bonus(self):
        return self.get_salary()*0.20
class developer(employee):
    def calculate_bonus(self):
        return self.get_salary()*0.15

manager=manager("rahul",50000)
developer=developer("aman",40000)
print("manager:",manager.name)
print("salary:",manager.get_salary())
print("bonus:",manager.calculate_bonus())
print()
print("developer:",developer.name)
print("salary:",developer.get_salary())
print("bonus:",developer.calculate_bonus())

        
