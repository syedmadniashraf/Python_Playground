try:
    a = int(input("heyy, Enter a number: "))
    print(a)

except ValueError as v:
    print("Heyyy")
    print(v)
    
except Exception as e:
    print(e)
print("Thank You")
