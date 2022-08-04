def interests():
    print(
        "Enter all your interests, one after the other and enter \"stop\" when done."
    )
    s1 = set()
    while True:
        interest = input()
        if interest.lower() == "stop":
            break
        else:
            s1.add(interest)
    return s1


#while interest.lower() != "stop":
#  interest = input()
#  if interest.lower() != "stop"
#    s1.add(interest)
#return s1
#print(interest())
def tinderDaSecond():
    print("First Person: ")
    p1 = interests()
    print("Second Person: ")
    p2 = interests()
    common = p1.intersection(p2)
    if len(common) >= 3:
      print(f"Yay - you are a match made in heaven! You have {len(common)} commmon interest")
    else: print("Oh no - there is no way it will work out :(")

tinderDaSecond()