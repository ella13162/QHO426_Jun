def dimentions():
  w = float (input("Enter width: "))
  l = float(input("Enter lendth: "))
  area = l*w
  return area
  # or return l*W
def r_name():
  return input("Enter the name of the room: ")
def price(name, area):
  if name.lower() == "bedroom": 
    return 10*area
  elif name.lower() == "bathroom":
    return 20*area
  elif name.lower() == "living room":
    return 12*area
  else:
    return 5*area

def run():
  t_price = 0
  num = int(input("How many rooms to clean?"))
  for i in range(num):
    name = r_name()
    area = dimentions()
    sub_price = price(name, area)
    t_price += sub_price
  print(f"Total to be paid: £{t_price:.2f}")
run()