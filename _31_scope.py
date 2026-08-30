# scope in python
'''
    Program ka woh area jahan kisi variable ko access (use) kiya ja sakta hai.
    Aregion that a variable is recongnized a iterable
    is only avaliable from inside from the region .

    (LEGB) are the fure variables are used in python mostly
    L=local
    E=enclosing
    G=global
    B=built-In

'''
# Local variable 
'''
    local variable which is acceptable only inside the function.
'''
print("-----------------")
print("local variable ")
def hello():
    x=34
    print("this the the local variable ", x)
hello()
# print(x) you can not access from the outside 

print("-----------------")
print("enclosing  variable ")
'''
    It is used inner sied of the function but changeable by using nonlocal keyword.
'''
def outer():
    y=45
    def inner():
        print(y)
    inner()
    print(y)
outer()
print("-----------------")
def outerr():
    z=1122  #local
    def innerr():
        nonlocal z
        z=2211 #enclosing
        print(z)
    innerr()
    print(z)
outerr()
'''
note:
    if change the value print also time is changeable value.
'''
print("-----------------")
print("Global variable ")
'''
    global variable is define at the top  of the programme .
    it can be modify by using 'gobal' keyword.
'''
i=344
def hellow():
    print(i)
hellow()
print(i)

print("-----------------")
j=9876
def hell():
    global j
    j=6789
    print(j)
hell()
print(j)

print("-----------------")
name = "Global"
def outer():
    name = "Enclosing"
    def inner():
        name = "Local"
        print(name)
    inner()
outer()
print(name)

