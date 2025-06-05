# 7. If the names of 2 friends are same; what will happen to the program in problem 6?


d = {}

name = input("Enter the name: ")
lang = input("Enter the language: ")

d.update({name:lang})
name = input("Enter the name: ")
lang = input("Enter the language: ")

d.update({name:lang})
name = input("Enter the name: ")
lang = input("Enter the language: ")

d.update({name:lang})
name = input("Enter the name: ")
lang = input("Enter the language: ")

d.update({name:lang})

print(d)

# The values entered later will be updated.