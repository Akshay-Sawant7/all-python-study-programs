'''def decor(func):
    def inner(name):
        if name=="xyz":
            print("xyz u r welcomed")
        else:
            func(name)
    return inner
@decor
def deco(name):
    print("hello",name,"u r not welcomed")
deco("raj")
deco("rohit")
deco("xyz")'''

#eg 2
'''def divideby0(funct):
    def inner(a,b):
        if b==0:
            print("dont provide zero")
        else:
            return funct(a,b)
    return inner
@divideby0
def division(a,b):
    return a/b
print(division(10,0))
'''

#eg 3
def first(msg):
    print(msg)
first("Hello")

second=first
second("hello")


