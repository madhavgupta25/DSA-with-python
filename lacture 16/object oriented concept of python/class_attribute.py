class customer:
    def __init__(self, name:str, age:int, gender:str, balance:float):
        self.name = name
        self.age = age
        self.gender = gender
        self.balance = balance
    
    def describe(self):
        info = f"name = {self.name}, age = {self.age}, gender = {self.gender}, balance = {self.balance}"
        print(info)

    def __str__(self):
        info = f"name = {self.name}, age = {self.age}, gender = {self.gender}, balance = {self.balance}"
        return info

c1 = customer('Madhav' , 20, 'Male', 1000.99)
c1.describe()
print(c1)
c2 = customer('Madhavi' , 20, 'Female', 10000.99)
c2.describe()