from inhabitant import Inhabitant

#Blueprint for a Human object
class Human(Inhabitant):

    #Initialiser/constructor of a class
    def __init__(self, name = "Human", age=0):
        #Instance attributes
        super().__init__(name, age)

    def __str__(self):
        return f"Human {self.name} is {self.age} years old and has energy {self.energy}"

    def __repr__(self):
        return f"Human(name={self.name}, age={self.age})"
        
    #Instance Method
    def display(self):
        print(f"I am {self.name}")


if __name__ == "__main__":
    h = Human("Frank")
    h.display()
    h.eat(0.75)
    h.grow()
    print(h)
    h.move(56)
    print(h)