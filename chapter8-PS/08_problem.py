# 8. Write a python function to print multiplication table of a given number.

def multiple(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

multiple(5)