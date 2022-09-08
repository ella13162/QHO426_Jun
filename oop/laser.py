from tech import Tech


class Laser(Tech):

  MAX_RANGE = 100

  def __str__(self):
    return f"I am a Laser of range {Laser.MAX_RANGE} m."

  def __repr__(self): 
    return "Laser()"
 # def __init__(self): we don't have atributes
  def fire (self, range):
    if range <= Laser.MAX_RANGE:
      print("Laser hits the target!")
    else:
      print("Target is to far away!")

  def activate(self):
    print("Laser ready to use!")

  def deactivate(self):
    print("Laser is off!")

if __name__ == "__main__":
  l = Laser()
  l. activate()
  l.fire(75)
  l.fire(150)
  l.deactivate()
  print(l)
 