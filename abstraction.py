#abstract method

'''from abc import *
class test :
    @abstractmethod
    def m1(self):pass


t= test()
t.m1()
'''

#abstract class

'''from abc import *
class Demo:
    @abstractmethod
    def m1(self):
        pass
class child(Demo):
    def m1(self):
        print("hello")
class child1(Demo):
    def m1(self):
        print("hii")
c1=child1()
c1.m1()
c=child()
c.m1()'''

'''from abc import*
class Parent:
    @abstractmethod
    def abs(self):
        pass
class class1(Parent):
    def abs(self):
        print("this is class 1")

class class2(Parent):
    def abs(self):
        print("this is class 2")
p=Parent()
c2=class2()
c2.abs()
c1=class1()
c1.abs()'''

'''from abc import *
class test :
    @abstractmethod
    def m1(self):pass

class child1(test):
   def m1(self):
       return 100;

class parent(test):
    def m1(self):
        return 1000;

c1=child1()
p=parent()
print(c1.m1())
print(p.m1())
'''

#practice eg

'''from abc import ABC, abstractmethod
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("i can walk and run")
class snake(animal):
    def move(self):
        print("i can crawl")
class dog(animal):
    def move(self):
        print("i can bark")
class lion(animal):
    def move(self):
        print("i can roar")
r=human()
r.move()

k=snake()
k.move()

r=dog()
r.move()

k=lion()
k.move()'''

#
'''from abc import *
class demo:
    @abstractmethod
    def m1(self):
        pass
    @abstractmethod
    def m2(self):pass
class child(demo):
    def m1(self):
        print("this is child implementation")
    def m2(self):
        print("this is m2 method implementation of child class")
class child1(demo):
    def m1(self):
        print("this is child1 class implementation")
    def m2(self):
        print("this is m2 method implementation of child1 class")
c=child()
c.m1()
c.m2()
c1=child1()
c1.m1()
c1.m2()'''

#
'''class test:
    def m2(self,a):
        print(a)
class test1(test):
    def m1(self):
        print("hello")

t=test1()
t.m2(10)
'''

#
'''class test:
    a=10
    _b=20
    __c=30

    def __init__(self):
        self__c=30
    def m1(self):
        print(test.a)
        print(test._b)
        print(test.__c)
t=test()
t.m1()
print(test.a)
print(test._b)
print(t._test__c)
'''


#__str__() method:
'''
class student :
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno

    def __str__(self):
        return 'this is student name:{} and Roll nO :{}' .format(self.name,self.rollno)

s1=student("abc",101)
s2=student("xyz",102)

print(s1)
print(s2)
'''
