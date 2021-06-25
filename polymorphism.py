'''Polymorphism : poly means many morphism means format
--------------------------
three types of polymorphism :-
------------------------------
1)overloading
2)overriding
3)datahiding
'''

#overloading-function with same name & different parameter
'''class Demo:
    def m1(self,a,b):
        print("two arg")
    def m1(self):
        print("zero arg")
    def m1(self,a):
        print("one arg")
d=Demo()
d.m1(10)'''

#notes
'''class parent:
    def __init__(self,x):
        self.x=x
    def __add__(self, other):
        return self.x + other.x

p1=parent(100)
p2=parent(200)
print(p1+p2)'''

#notes
'''class parent:
    def __init__(self,x):
        self.x=x
    def __gt__(self, other):
        return self.x > other.x

p1=parent(100)
p2=parent(200)
print(p1>p2)'''


#overriding

'''class Student:
    def m1(self, a =None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("the sum of the three nos is :" , a+b+c)
        elif a!=None and b!=None:
            print("the sum of the two no is :" , a+b)
        else :
            print("plz provide correct arguments ")


s=Student()
s.m1(10,20,30)'''

'''class test:
    def sum(self,*a):
        total=0
        for x in a :
            total=total+x
            print("the sum of the no is : " , total)

t = test()
t.sum(10,20)'''

'''class Student:
    def __init__(self):
        print("this is a constructor")
s=Student(10,20,30,40,50,60)''' #error

'''class Test:
    def __init__(self,a=None,b=None,c=None):
        print("this is a constructor")
t=Test(10,20,30) '''


#notes
'''class Student:
    def m1(self):
        print("zero - arg ")
    def m1(self,a):
        print("one - arg")
    def m1(self,a,b):
        print("two - arg ")

s=Student()
s.m1(10,20)'''

#notes
'''class Student:
    def m1(self, a =None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("the sum of the three nos is :" , a+b+c)
        elif a!=None and b!=None:
            print("the sum of the two no is :" , a+b)
        else :
            print("plz provide correct arguments ")


s=Student()
s.m1()
'''
#notes
'''class test:
    def sum(self,*a):
        total=0
        for x in a :
            total=total+x
            print("the sum of the no is : " , total)

t = test()
t.sum(10,20,10,100)
'''
#data hiding
#notes
'''class Test:
    def __init__(self):
        print("this is default constructor ")

    def __init__(self,a):
        print("this is onr - arg  constructor ")

    def __init__(self,a,b):
        print("this is two- arg constructor ")

t= Test(10,20)'''

#notes
'''class Test:
    def __init__(self,a=None,b=None,c=None):
        print("this is a  constructor ")
t= Test(10)'''

#notes
'''class Student :
    def __init__(self,*a):
      print("this is a constructor ")
s=Student(10,20)
'''

'''class parent:
    def m1(self):
        print("heelo")
class child(parent):
    def m1(self):
        print("hi")
c=child()
c.m1()'''

#class sir pract
'''poly means many
morphism means format
1 overloading
2 overriding
3 DataHiding

#overloading - not supported in python

function with same name and different parametrs'''
'''
class demo:
    def m1(self):
        print("zero arg")
    def m1(self,a):
        print("one arg")
    def m1(self,a,b):
        print("two arg")
d=demo()
d.m1(10)
d.m2(10,20)'''

'''class test:
    def sum(self,*a):
        total=0
        for x in a :
            total=total+x
        print("the sum of the no is : " , total)

t = test()
t.sum(10,20,10,100)

#
def m1(*a):
    print("hello")
m1(10,20,30)
'''

'''class Student:
    def m1(self, a =None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print("the sum of the three nos is :" , a+b+c)
        elif a!=None and b!=None:
            print("the sum of the two no is :" , a+b)
        else :
            print("plz provide correct arguments ")

s=Student()
s.m1()

def m1(a=10):
    print("hello",a)
m1(20)'''

#constructor overloading - not supported in python
'''class Test:
    def __init__(self):
        print("this is default constructor ")

    def __init__(self,a):
        print("this is onr - arg  constructor ")

    def __init__(self,a,b):
        print("this is two- arg constructor ")

t= Test(10,20)
'''
#resolution of this
'''class Student:
    def __init__(self, *a):
        print("this is a  constructor ")

s=Student(10,20,30,40,50,60)'''

class Test:
    def __init__(self,a=None,b=None,c=None):
        print("this is a  constructor ")
t= Test(10,20,30)

#overriding - function with same name and same parametrs'''

'''class parent:
    def m1(self):
        print("heelo ")   

class child(parent):
    def m2(self):
        print("hi")

c= child()
c.m1()
'''


