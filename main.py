#the calss person which will be blueprint for my objects to store information about humans/people
class Person:

  #initialiser/ constructor mehtod is authomaticly invoced immediately when object is created and is one of magic method
  #initialiser of any class has the same name
  #dunder = __ double underscore
  def __init__(self):
    #below are instance attributes, just fitures of any person
    self.name = "piotr"
    self.age = 0
    self.job = "non"
    self.weight = 1