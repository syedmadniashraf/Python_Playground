class Employee:
    language = "Python" # This is a class attribute
    salary = 1200000

    def __init__(self, name , language, salary):  # Dunder method which is automatically called
        self.name = name
        self.language = language
        self.salary = salary
        print("I am creating an object")

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet():
        print("Good Morning")


harry = Employee("Harry", "JavaScript", 1200000)
# harry.name = "Harry"
print(harry.name, harry.language, harry.salary)

# rohan = Employee( )



