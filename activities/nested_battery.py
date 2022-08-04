print("I need to find spare battery.")
print("Where should I look?")
place = input()
if (place == "in the bedroom"):
  print("Where {} should I look".format(place))
  bedrooom_place = input()
  if (bedrooom_place == "under the bed"):
    print("Found some shoes but not battery.")
  else:
    print("Found some mess but not battery.")

if (place == "in the bathroom"):
  print("Where {} should I look".format(place))
  bathroom_place = input()
  if (bathroom_place == "in the bathtub"):
    print("Found a rubber duck but no battery.")
  else:
    print("Found a wet surface but no battery.")

if (place == "in the lab"):
  print("Where {} should I look".format(place))
  lab_place = input()
  if (lab_place == "on the table"):
    print("Yes! I found my battery!")
  else:
    print("Found some tools but no battery.")
else:
  print("I do not know where that is but I will keep looking.")