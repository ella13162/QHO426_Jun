import matplotlib.pyplot as plt
import matplotlib.animation as a
import numpy as np

fig, ax = plt.subplots()

def animate(f):
  ax.set_ylim(-1, 1)
  ax.set_xlim(0, 720)
  x_degree = np.arange(0, f)
  x_rad = x_degree * np.pi / 180
  y = np.sin(x_rad)
  ax.plot(x_degree, y, "r")

def animate2(f):
  ax.set_ylim(-1, 1)
  ax.set_xlim(0, 720)
  x_degree = np.arange(0, f)
  x_rad = x_degree * np.pi / 180
  y = np.cos(x_rad)
  ax.plot(x_degree, y, "b")

def run():
  harry = a.FuncAnimation(fig, animate, frames = 720, interval = 10)
  mark = a.FuncAnimation(fig, animate2, frames = 720, interval = 10)
  plt.show()
  
run()
  