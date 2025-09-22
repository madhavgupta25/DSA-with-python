# in this lacture we will the concept of class and object in python

class customer:
    def __init__(self, name:str, age:int, gender:str, balance:float):
        self.name = name
        self.age = age
        self.gender = gender
        self.balance = balance
        pass
    pass

c1 = customer('Madhav' , 20, 'Male', 1000.99)
c2 = customer('Madhavi' , 20, 'Female', 10000.99)
print(f"name={c1.name}, age={c1.age}, gender={c1.gender}, balance={c1.balance}")
print("name")