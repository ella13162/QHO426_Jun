import matplotlib.pyplot as plt
def coordinate():
  x = float(input("Enter x value: "))
  y = float(input("Enter y value: "))
  return x,y

def path():
  print("Retrievieng path...")
  x_values = []
  y_values = []
  for i in range (4):
    data = coordinate()
    x_values.append(data[0])
    y_values.append(data[1])
  return[x_values, y_values]

def run():
  values = path()
  plt.plot(values[0], values[1], "ro--")
  plt.xlabel("x values")
  plt.ylabel("y values")
  plt.show()
run()