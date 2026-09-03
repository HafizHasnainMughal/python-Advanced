# Inheritence in class
'''
    Ek class doosri class ki properties (attributes) aur behaviors 
    (methods) ko inherit/use kar sakti hai.
    Inheritance mein usually do important terms hoti hain.
    Parent Class:
        Jis class se features inherit kiye jate hain.
        Isko kehte hain:
            Parent Class
            Base Class
            Superclass
    Child Class:
        Jo parent se features inherit karti hai.
        Isko kehte hain:
            Child Class
            Derived Class
            Subclass

    basic syntex:
    class parent:
        pass
    class child(parent):
        pass
'''
print("------------------")
print("simple inheritence class with method ")

class animal:
    def eat(self):
        print("animal is eating ")
class dog(animal):
    def bark(self):
        print("dog is wawo wawo and barking also ")
a=animal()
a.eat()
b=dog()
b.bark()

print("------------------")
print("simple inheritence class with constructor only parent  ")

class P_class:
    def __init__(self,name):
        self.names=name
    def eat(self):
        print(self.names,"is eating ")
class c_class(P_class):
    def bark(self):
        print(self.names,"is barking and wawoo wawoo also")
a1=c_class("tommy")
a1.eat()
a1.bark()

print("------------------")
print("simple inheritence class with constructors ")
class Animal:
    def __init__(self,name):
        self.P_name=name
        print(f"the animal name is {self.P_name}")
class Dog(Animal):
    def __init__(self, name,breed):
        super().__init__(name)
        self.breed=breed
        print(f"the {self.P_name}  breed is {self.breed }")
obj1=Dog("tommy","penter ")

print("------------------")
print("simple inheritence class with constructors also user input ")
class Animall:
    def __init__(self):
        self.P_name=input("enter your animal name: ")
        print(f"the animal name is {self.P_name}")
class Dogg(Animall):
    def __init__(self, ):
        super().__init__()
        self.breed=input("enter your animal breed type: ")
        print(f"the {self.P_name}  breed is {self.breed }")    
oje1=Dogg()

print("------------------")
print("the simple and complete example ")

class Employee:
    def __init__(self):
        self.employee_id = int(input("enter the employee id: "))
        self.name = input("enter the employee name: ")
        self.department = input("enter the employee department: ")
        self.basic_salary = float(input("enter the employee basic salaery: "))
    def display_info(self):
        print("\n----- EMPLOYEE INFORMATION -----")
        print("Employee ID:", self.employee_id)
        print("Name:", self.name)
        print("Department:", self.department)
        print("Basic Salary:", self.basic_salary)
    def calculate_salary(self):
        print("Basic Salary:", self.basic_salary)

class Worker(Employee):
    def __init__(self):
        super().__init__()
        self.overtime_hours = float(input("enter the employee overtime hours: "))
        self.overtime_rate = float(input("enter the employee overtime rate: "))
    def display_info(self):
        super().display_info()
        print("Overtime Hours:", self.overtime_hours)
        print("Overtime Rate:", self.overtime_rate)
    def calculate_salary(self):
        overtime_pay = (
            self.overtime_hours
            * self.overtime_rate)
        total_salary = (
            self.basic_salary
            + overtime_pay)
        print("Total Salary or worker:", total_salary)
        print("overtime pay worker :",overtime_pay)
class Supervisor(Employee):
    def __init__(self):
        super().__init__()
        self.bonus = float(input("enter the supervisor bouns:"))
    def display_info(self):
        super().display_info()
        print("Bonus:", self.bonus)
    def calculate_salary(self):
        print("Total Salary of the supervisor:", ( self.basic_salary + self.bonus))
class Manager(Employee):
    def __init__(self):
        super().__init__()
        self.performance_bonus = float(input("enter the manager performance bouns: "))
        self.allowance = float(input("enter the manager allowance: "))
    def display_info(self):
        super().display_info()
        print("Performance Bonus:", self.performance_bonus)
        print("Allowance:", self.allowance)
    def calculate_salary(self):
        print("Total Salary of the manager:",
               ( self.basic_salary + self.performance_bonus + self.allowance))
# worker1=Worker()
# worker1.display_info()
# supervisor=Supervisor()
# supervisor.display_info()
manager=Manager()
manager.display_info()
manager.calculate_salary()