import matplotlib.pyplot as plt
import matplotlib.animation as animation

def animate(frame):
  print(frame)

def run():
  fig, ax = plt.subplots()
  bob = animation.FuncAnimation(fig, animate, interval = 1000, frames = 10, repeat = False)
  #if i don't write repeat = False then it will never stop
  plt.show()

run()