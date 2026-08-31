# intense variable  in class 
'''
    Instance Variables wo variables hote hain jo har object (instance)
      ke liye alag aur unique hote hain.

    Jab aap ek class se multiple objects banate hain, toh har object ka apna data hota hai
    . Un sabhi unique details ko store karne ke liye instance variables ka use hota hai.
    jo variable self.variable_name

    intence variable always define the self.variable_name
    Ek object ke instance variable ki value badalne se dusre object par koi farq nahi padta.

'''
print("---------------------")
print("intence variables in class ")
class Student:
    def __init__(self, name, age):
        self.name = name   # Ye dono Instance Variables hain
        self.age = age
# Object 1
student1 = Student("Ali", 20)
# Object 2
student2 = Student("Sara", 22)
print(student1.name)  
print(student2.name) 
# Ek object ki value change karna
student1.name = "Hamza"
print(student1.name) 
print(student2.name)
