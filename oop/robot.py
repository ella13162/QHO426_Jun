from inhabitant import Inhabitant

class Robot(Inhabitant):

    def __init__(self, name = "Robot"):
        super().__init__(name)

    def __str__(self):
        return f"Robot {self.name} is {self.age} years old and has energy {self.energy}"

    def __repr__(self):
        return f"Robot(name={self.name}, age={self.age})"

    def display(self):
        print(f"I am {self.name}")

if __name__ == "__main__":
    rob = Robot("Wall-E")
    rob.display()
    print(rob)
    print(repr(rob))
    rob.eat(94)
    print(rob)
    rob.move(73)
    print(rob)
    rob.eat(256)
    print(rob)
    rob.move(101)
    rob.grow()
    rob.grow()
    print(rob)