import matplotlib.pyplot as plt
import matplotlib.animation as a
import random
fig, ax = plt.subplots()

def animate(f):
  colours = ["y", "b", "g", "r"]
  colour = colours[random.randint(0, 3)]
  ax.set_ylim(0, 10)
  ax.set_xlim(0, 10)
  
  ax.plot(f, f, colour + "o")
  #we can change second f if we want regular line 

def run():
  fred = a.FuncAnimation(fig, animate, interval = 1000, frames = 10)
  plt.show()

run()