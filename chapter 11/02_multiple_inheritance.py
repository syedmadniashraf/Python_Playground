class Employee:
    company = "ITC"
    name = "Default name"
    
    def show(self):
        print(f"The name of the Employee is {self.name} and the company is {self.company}")


class Coder:
    language = "Python"
    
    def printLanguage(self):
        print(f"Out of all the languages, here is your language: {self.language}")


class Programmer(Employee, Coder):
    company = "ITC Infotech"
    
    def showLanguage(self):
        print(f"The name is {self.name}, works at {self.company}, and is good with {self.language} language")


# Creating instances
a = Employee()
b = Programmer()

# Calling methods
b.show()
b.printLanguage()
b.showLanguage()
