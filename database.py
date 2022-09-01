from person import Person 

class Database:
  
  def __init__(self, name):
    self.name = name +" 's database'"
    self.people = []
    self.no_ppl = len(self.people)
    
  def add_person(self, p):
    self.people.append(p)
    self.no_ppl += 1

  def remove_person(self, p):
    if p in self.people:
      self.people.remove(p)
    else: 
      print("Person not in database")
  def display_all_ppl(self):
    for person in self.people:
      print(person)

p1 = Person("Zaki", 41, "truck driver", 78)
p2 = Person("Katia", 32, "Waitress", 55)
p3 = Person("Garry", job="Manager", weight = 175)
print("-"*20)
db = Database("Piotr")
db.add_person(p1)
print("-"*20)
db.display_all_ppl()
db.add_person(p3)
db.display_all_ppl()
print("-"*20)
db.remove_person(p1)
db.display_all_ppl()
print("-"*20)
db.add_person(p2)
db.display_all_ppl()


  