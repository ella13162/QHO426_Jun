print("Please enter an eye character:")
eye = input() 
print("Please enter the length of the glasses:")
length = int(input())
print()

print(f"#########{' ' * length}#########")
print(f"#   {eye}   {'#' * (length + 2)}   {eye}   #")
print(f"#########{' ' * length}#########")

print()