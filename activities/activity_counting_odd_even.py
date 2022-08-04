print("Please neter first whole number: ")
first_number=float(input())
print("Please enter second whole number: ")
second_number=float(input())
print("Please enter third whole number: ")
third_number=float(input())

odd_number = 0
even_number = 0

if first_number % 2 == 0:
  even_number = even_number + 1
else: 
  odd_number = odd_number + 1

if second_number % 2 == 0:
  even_number = even_number + 1
else:
  odd_number = odd_number + 1

if third_number % 2 == 0:
  even_number = even_number + 1
else:
  odd_number = odd_number + 1

print("Tere were {} even numbers and {} odd numbers in this set.".format(even_number, odd_number))
  

