from tech import Tech


class Jetpack(Tech):

  def __str__(self):
    return "I am a Jetpack."

  def __repr__(self): 
    return "Jetpack()"
 # def __init__(self): we don't have atributes

  def activate(self):
    print("Jetpack is on!")

  def deactivate(self):
    print("Jetpack is off!")

  def fly (self, speed):
    print(f"We fly at {speed} m/s.")

if __name__ == "__main__":
  jet = Jetpack()
  jet. activate()
  jet.fly(10)
  jet.fly(25)
  jet.deactivate()
  print(jet)
 