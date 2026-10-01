# abstraction method in oop(object oriented programming)
'''
    Abstraction ka asali maksad hai "Kya karna hai" (What to do) ye dikhana,
      aur "Kaise karna hai" (How to do it) ye chhupa lena.
    Jab aap bade projects par kaam karte hain, toh aap chahte hain ki ek standard
      design follow ho aur unnecessary details end-user ya dusre developers ko distract na karein.

    syntex:
        from abc import ABC,abstractmethod
      
'''
print("----------------")
from abc import ABC,abstractmethod
class car(ABC):
    @abstractmethod
    def engine_type(self):
        pass
    @abstractmethod
    def engine_capacity(self):
        pass
class BMW(car):
    def engine_type(self):
        print("BMW has petrol engine")
    def engine_capacity(self):
        print("BMW has 3.0L engine capacity")
class mercedes(car):
    def engine_type(self):
        print("Mercedes has diesel engine")
    def engine_capacity(self):
        print("Mercedes has 2.0L engine capacity")
class toyota(car):
    def engine_type(self):
        print("Toyota has hybrid engine")
    def engine_capacity(self):
        print("Toyota has 1.8L engine capacity")
create_obj_bmw=BMW()
print("----------------")
create_obj_bmw.engine_type()
create_obj_bmw.engine_capacity()
print("----------------")
create_obj_mercedes=mercedes() 
create_obj_mercedes.engine_type()
create_obj_mercedes.engine_capacity()
print("----------------")
create_obj_toyota=toyota()
create_obj_toyota.engine_type()
create_obj_toyota.engine_capacity()