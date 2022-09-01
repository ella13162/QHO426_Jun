with open("song.txt", "r") as song:
  s = song.read()
# print(s)
  s1 = s.lower().replace(", ", "").split() 
# it change into list and with .lower() it will change all words with upper case to lower case
#.replace can change specific character to something else
  print(s1)
  print("~"*30)
  print(set(s1)) #doesn't allow the same words to repead
  print("~"*30)

  dictio = {}
  for token in s1:
    dictio [token] = dictio.get(token, 0) +1
    #token is a key word// . get is the method to access the value
  print(dictio)
  print("~"*30)
  print(f"To write the viral song we need {len(set(s1))} of the unique words.")
  