# OOP (Object-Oriented Programming)
'''
    Programming ka ek style jisme hum real-world entities ko
    Objects aur Classes ki form mein represent karte hain.

    In oop by using a class in which having many different
    clid having their own properties.
    In this case we  use class objects.

    Class ek blueprint (template) hoti hai.
    Attributes  > object ki properties or data  hota hay 

'''

print("----------------")
print("simple oop structure ")
class person:     # person is the class name
    name="Mughal" # }
    age=23        # } blue print
    sex="Male"    # }
a=person()        # object created
b=person()
print(a.name)     #calling name form blue print
print(a.age)
print(a.sex)

print("----------------")
print("attributes in class")
class students:
    pass
first_student=students()
first_student.name="hassan".title()
first_student.age=23
print(first_student.name)
print(first_student.age)



