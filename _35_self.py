# self in class 
'''
    self current object ko represent karta hai.
    Note:
    1> Class ke andar jab bhi aap koi normal method (function) banate hain,
      usme pehla parameter self hona lazmi hai.
    2> Jab aap method ko object ke zariye call karte hain, toh Python self ki value 
      automatically pass kar deta hai.
      Aapko manual pass karne ki zaroorat nahi hoti.
    3> self koi fixed keyword nahi hai  Aap iski jagah koi aur naam bhi rakh sakte hain,
      lekin Python community mein standard practice self hi hai.

'''
print("-----------------")
print("simple self code ")
class car:
    def __init__(self,brand,color):
        self.brands=brand
        self.colors=color
    def display_data(self):
        print(f"Car Brand: {self.brands.upper()}, Color: {self.colors.title()}")
car1=car("BMW","Black")
car2=car("mercedes","blue")
car3=car("toyota","white")
car1.display_data()
car2.display_data()
car3.display_data()