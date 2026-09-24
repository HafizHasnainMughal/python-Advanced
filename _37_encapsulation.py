# Encapsulation in class
'''
    Encapsulation Object-Oriented Programming (OOP) ka ek core concept hai,
     jiska matlab hai Data (variables) aur Methods (functions) ko 
     ek single unit (Class) mein pack kar dena aur outer access ko control karna.

    Encapsulation is the process of bundling data and methods that operate on that data into a single unit,
    while controlling access to the internal data.

    Two main points:
        Data Grouping: Related variables aur functions ko ek jagah rakhna.
        Data Hiding (Protection): Sensitive data ko class ke bahar se
          direct access ya modify hone se rokna.
'''
# private variable
'''
    private variable ko class ke bahar se access nahi kiya ja sakta.
    isko double underscore kay sath define kiya jata hai, like __variable_name.
    private variable ko class ka under hi access kiya ja sakta hai,
      aur class ke bahar se direct access nahi kiya ja sakta but using getter and setter methods.

'''
print("----------------")
# simple example for private variable
class person:
    def  __init__(self,name,age):
        self.__name=name
        self.__age=age
    def display_data(self):
        print(f"Name:{self.__name}, Age: {self.__age}")
a=person("Ali",24)
a.display_data()
# print(a.__name)  # ye error dega, kyuki __name private variable hai

print("----------------")
# complete example for private variable with getter and setter methods
class student:
    def __init__(self,name,age,grade):
        self.__name=name
        self.__age=age
        self.__grade=grade
    def get_data(self):
        return self.__name,self.__age,self.__grade          
    def set_data(self,name,age,grade):
        self.__name=name
        self.__age=age
        self.__grade=grade
first_student=student("Hassan",20,"A")
print(f"first student data : {first_student.get_data()}") #ya data show kary ga
student.set_data(first_student,"Hassan",20,"B") #ya data update kary ga
print(f"first student data after update : {first_student.get_data()}") #ya updated data show kary ga

# protected variable 
'''
    protected variable ko class ka bahir use kiya ja sakta hay but
      derived class kay through hi access kiya ja sakta hay.
    protected variable ko single underscore kay sath define kiya jata hay,like _variable_name.

'''
print("----------------")
# simple example of protected variable
class Student:
    def __init__(self):
        self._name="Ali"
        self._age=25
    def display_data(self):
        print(F"Name of the student is {self._name} and age is {self._age}")
a1=Student()
a1.display_data()
print(a1._name) #ya direct access kary ga, but ye best practice nahi hay