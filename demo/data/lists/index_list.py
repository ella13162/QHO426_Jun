def movements():
  return ["move forward", 10 , "move backwards", 5 , "move left", 3 , "move right", 1 ]
  

def run():
  print("moving...")
  micky_mouse = movements()
  for i in range (0, len(micky_mouse), 2):
    print(f"{micky_mouse[i]} for {micky_mouse[i+1]} steps")
run()
