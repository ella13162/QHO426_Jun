print("Program started!\n")
print ("Please enter an ASCII code: ")
x = abs(int(input ()))
if x in range(32,127):
        print(f"The charracter represented by the ASCII code {x} is {chr(x)}")
print("The program ended!")