# Method in class
'''
    method ik function hi hota hay but ya class kay under define kiya jata hay
    class ka object create kar kay call kiya jata hay.

'''
print("methods in class ")
print("---------------")
class persn:
    def person_data(self):
        self.name='hassan'.title()
        self.age=23
        self.education="BS-Cs"
    def display(self):
        print(f"your name is {self.name} ")
        print(f"your age is {self.age} ")
        print(f"your education is {self.education} ")
a=persn()
a.person_data()  #object.method_name
a.display()      #object.method_name

print("---------------")
print("user input in method ")
print("---------------")
class persons:
    def input_data(self):
        self.names=input("enter your name ").title()
        self.ages=input("enter your age ")
        self.educations=input("enter your education level ").capitalize()
    def data_diplay(self):
        print("your entered data are : ")
        data=[self.names,self.ages,self.educations]
        for x in data:
            print(x,end=" ")
first_person=persons()
first_person.input_data()
first_person.data_diplay()

print("---------------")
'''
    function vs method
    function > jo class kau bahir define kiya jata hay or is ka koi 
     object kay sath call nahi kiya jata hay.
    method > jo class kay under define kiya jata hay or object kay sath call hota hay.
'''
print("---------------")
print("simple function ")

def hellow():
    name="mughal"
    print(name)
hellow()