# Constructor in python classes
'''
    Constructor ek special method hai jo object create hote hi automatically run hota hai.
    or ya ik class my only one hota hay .
    syntex:
        def __init__(self):
'''
print("---------------")
print("constructors in class simple code  ")
class student:
    def __init__(self):
        print("you created the first constructor horayyyyyyyyy! ")
first=student()

print("---------------")
class persn:
    def __init__(self):
        self.name='hassan'.title()
        self.age=23
        self.education="BS-Cs"
    def display(self):
        print(f"your name is {self.name} ")
        print(f"your age is {self.age} ")
        print(f"your education is {self.education} ")
a=persn()
a.display()






