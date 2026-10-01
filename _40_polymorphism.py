# Polymorphism method in oop
'''
    Polymorphism do words se bana hai: Poly (Bahut saare) aur Morph (Roop).
    Iska matlab hai ki ek hi function, method, ya operator alag-alag objects ke sath
      alag-alag behave karega.
    Python me polymorphism bohot naturally kaam karta hai kyunki Python ek
      dynamically typed language hai (ise Duck Typing bhi kehte hain).

'''
print("----------------")
# simple example of polymorphism 
print("---------------------")
print("polymorphism in oop")
class dog():
    def speak(self):
        print("Bhow Bhow")
class cat():
    def speak(self):
        print("Meow Meow")
class cow():
    def speak(self):
        print("Moo Moo")
class lion():
    def speak(self):
        print("Roar Roar")

print("---------------------")
obj_dog=dog()
obj_dog.speak()
print("---------------------")
obj_cat=cat()
obj_cat.speak()
print("---------------------")
obj_cow=cow()
obj_cow.speak()
print("---------------------")
obj_lion=lion()
obj_lion.speak()

print("---------------------")
animals=[dog(),cat(),cow(),lion()]
for x in animals:
    x.speak() 

# polymorphism with inheritance
print("---------------------")
class animal():
    def speak(self):
        print("Animals are speaking ")
class dog(animal):
    def speak(self):
        print("wahoo wahoo ")
class cat(animal):
     def speak(self):
         print(" meow meow")
class lion(animal):
    def speak(self):
        print(" roar roar ")

obj1_animal=animal()
obj1_animal.speak()
obj2_dog=dog()
obj2_dog.speak()
obj3_cat=cat()
obj3_cat.speak()
obj4_lion=lion()
obj4_lion.speak()