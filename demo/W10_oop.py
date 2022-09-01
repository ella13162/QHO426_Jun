    def __init__(self, name = "", age = 0, job = "Unemployed", weight = 2):
        #Below are instance attributes (features of any Person)
        self.name = name
        self.age = age
        self.job = job
        self.weight = weight

    #Method - function attached to a specific data type
    #Instance method -> it applies to a specific instance of a class
    def eat(self, food, w):
        print(f"{self.name} have eaten {food}")
        self.weight += w
        print(f"{self.name} now weights {self.weight}kg")

    def exercise(self, burned):
        self.weight -= burned
        print(f"{self.name} has exercised and now weights {self.weight}kg")


p1 = Person("Tom")
p2 = Person("Beth", 25, "Accountant", 72)
print(p1)
print(p2)
print(f"Person called {p1.name} is {p1.age} years old and weight {p1.weight}kg")
print(f"Person called {p2.name} is {p2.age} years old and weight {p2.weight}kg")
p2.eat("Spaghetti", 2.3)
p2.eat("Sandwich", 0.3)
p2.exercise(1.5)
p1.eat("Pizza", 1.2)