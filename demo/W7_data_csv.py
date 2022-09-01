import csv
import matplotlib.pyplot as plt

def gather_data (n =1):
    with open("june_data.csv", "w")as file: # "w" is to write mode-create the file, and "a" is to append, while "r" only to read mode
      csv_writer= csv.writer(file)
      for i in range(n):
        h = float(input("Enter the height: "))
        w = float(input("Enter the weight: "))
        csv_writer.writerow([h, w]) # to separate height and weight in the rows

#gather_data(3) for testing
def retriev_data():
  with open("june_data.csv")as file:
    hs = []
    ws = []
    csv_reader = csv.reader(file)
    for row in csv_reader:
        hs.append(float(row[0]))
        ws.append(float(row[1]))
  return hs, ws

#print(retriev_data()) for testing
def graphs():
  x, y = retriev_data()
  plt.plot(x, y, "ro-")
  plt.show()

graphs()
      