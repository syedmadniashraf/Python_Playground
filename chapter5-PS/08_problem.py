# 8. If languages of two friends are same; what will happen to the program in problem 6?


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

# Nothing will happen. The values will be same.