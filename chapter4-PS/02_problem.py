# 2. Write a program to accept marks om 6 students and display them in a sorted
# manner.

marks = []

m1 = int(input('Enter marks name:'))
marks.append(m1)
m2 = int(input('Enter marks name:'))
marks.append(m2)
m3 = int(input('Enter marks name:'))
marks.append(m3)
m4 = int(input('Enter marks name:'))
marks.append(m4)
m5 = int(input('Enter marks name:'))
marks.append(m5)
m6 = int(input('Enter marks name:'))
marks.append(m6)

marks.sort()

print(marks)