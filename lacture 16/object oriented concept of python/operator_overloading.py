class Customer:
    def __init__(self, name:str, age:int, gender:str, balance:float):
        self.name = name
        self.age = age
        self.gender = gender
        self.balance = balance
    
    def __eq__(self, other):
        return (
            self.name == other.name
            and self.age == other.age
            and self.gender == other.gender
            and self.balance == other.balance
        )

c1 = Customer("Madhav", 20, "Male", 100.00)
c2 = Customer("Madhav", 20, "Male", 100.00)

if c1 == c2:
    print("Equal")
else:
    print("Not Equal")