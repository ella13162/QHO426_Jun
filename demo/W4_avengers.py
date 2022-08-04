def adding(lista =[]):
  new_member = input("Enter new avenger: ")
  lista.append(new_member)
def remove(lista = []):
  rejected = input("Enter avenger to be removed: ")
  if rejected in lista:
    lista.remove(rejected)

#lista =[]
#for i in range(3):
 # adding(lista)
#remove(lista)
#print(lista)
def printing(lista =[]):
  for hero in lista:
    print(f"The mighty {hero} is part of Avengers!")

#lista = ["ScoobyDoo", "Jerry", "Thor"]
#printing(lista)

def run():
  avengers =[]
  while True:
    opt = int(input("Avengers assemble!\n\n1.add a new Avenger\n2.remove Avenger\n3.Check on the team\n9.Exit\n"))
    if opt == 1:
      adding(avengers)
    elif opt == 2:
      remove(avengers)
    elif opt == 3:
      printing(avengers)
    elif opt == 9:
      break
    else:
      print("No much option exist! Try Again. Dummy.")
run()