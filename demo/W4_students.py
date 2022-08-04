def generate():
  name = input("Enter name: ")
  mrk = int(input("Enter final mark: "))
  return name, mrk
#generate()
#print(generate())
def list_students(n):
  student_list = []
  for i in range(n):
    student_list.append(generate())
  return student_list

#print(list_students(4))
def avg_mark(lista =[]):
    total = 0
    for tup in lista:
      total = total + tup[1] #(total++ tup[1])
    average = total/len(lista)
    return average
#x = avg_mark(list_students(3))
#print(f"Average was {x:.0f}") 
#.0f will give the whole amount without decimal
def run():
  stud_list = []
  while True:
      opt = int(input("Menu:\n1. Populate list of students\n2. Calculate Average Mark\n3. Change mark of a student\n4. Exit\n Option: "))
      if opt == 4:
        break
      elif opt == 1:
        num =int(input("Enter number of students: "))
        stud_list.extend(list_students(num))
      elif opt == 2:
        print(f"The average mark is {avg_mark(stud_list)}")
      elif opt == 3:
        name = input("Enter name of student: ")
        for student in stud_list:
          if student[0].upper() == name.upper():
            print(f"Enter new mark for {name}: ")
            n_mrk= int(input())
            stud_list.remove(student)
            #stud_list.append((name, n_mrk))
            stud_list.insert(0,(name, n_mrk))
      else:
        print("Choose again. You fool.")
run()
