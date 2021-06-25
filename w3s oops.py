'''
5 pillars of OOPs
1)class and Object
2)Inheritance
3)Polymorphism
4)Encapsulation
5)Abstraction
'''

# 1) class & object
#class : class is like an object constructor or a "blueprint" for creating objects.
'''class myclass:    #in this myclass is a class
    x=5
print(myclass)'''

#object
'''class myclass:
    x=95
p1=myclass()        #here p1 is object
print(p1.x)'''

# __init__() function
#object method
class student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def m1(self):
        print("hello my name is :", self.name)
        print("hello my age is :", self.age)
        print("hello my marks is :", self.marks)
    def m2(self):
        print("this is 2nd method")
st=student("jacky",35,88)
st.m1()
st.m2()

# 2) Inheritance
#inheritance allows us to define a class that inherits all the methods and properties from another class.
#Parent class : is the class being inherited from, also called base class.
#Child class : is the class that inherits from another class, also called derived class.

'''1)Simple inheritance:
2)Multi level Inheritance
3)Hierarchical Inheritance
4)Multiple Inheritance
5) cyclic Inheritance'''

# 3) 'Polymorphism : poly means many morphism means format
# --------------------------
# three types of polymorphism :-
# ------------------------------
# 1)overloading :- a)Operator overloading, b)Method Overloading, c)constructor overloading
# 2)overriding
# 3)datahiding

#1) overloading : function with same name & different parameter
#eg
class demo:
    def m1(self):
        print("zero arg")
    def m1(self,a):
        print("one arg")
    def m1(self,a,b):
        print("two arg")
d=demo()
d.m1(10)
d.m2(10,20)

#a)Operator overloading
class parent:
    def __init__(self,x):
        self.x=x
    def __add__(self, other):
        return self.x + other.x

p1=parent(100)
p2=parent(200)
print(p1+p2)

#b)Method Overloading: If two methods with same name but diffent arguments then it is
#said to be overloaded method.
class demo:
    def m1(self):
        print("zero arg")
    def m1(self,a):
        print("one arg")
    def m1(self,a,b):
        print("two arg")
d=demo()
d.m1(10)
d.m2(10,20)

#c)constructor overloading
class Test:
    def __init__(self):
        print("this is default constructor ")

    def __init__(self,a):
        print("this is onr - arg  constructor ")

    def __init__(self,a,b):
        print("this is two- arg constructor ")

t= Test(10,20)

#2)overriding : function with same name and same parametrs'''
# If child class is not happy with the parent class implementation then child
# class is allowed to redefined that method in the child class .This concept
# is known as Method Overriding.

class parent:
    def m1(self):
        print("heelo ")

class child(parent):
    def m2(self):
        print("hi")

c= child()
c.m1()

#3)data hiding: is the method to prevent access to specific users in the application.

class justcounter:
    __secretcount=0
    def count(self):
        self.__secretcount+=1
        print(self.__secretcount)
counter= justcounter()
counter.count()
counter.count()
#print(counter.__secretcount)
print(counter._justcounter__secretcount)

# 4) Encapsulation: the process of wrapping up variables and methods into a single entity is called

class parrot:
    def fly(self):
        print("parrot can fly")
    def swim(self):
        print("parrot cant swim")
class penguin:
    def fly(self):
        print("penguin cant fly")
    def swim(self):
        print("penguin can swim")
def flying_test(bird):
    bird.fly()

blu=parrot()
peggy=penguin()

flying_test(blu)
flying_test(peggy)


# 5) Abstraction
#  Abstract method
#  Abstract class
#  Interface
#  __str__() method
#  str () and repr() functions

# Abstract method:If we dont know about the implementation part so we can declare a method.
# such type of method is know as abstract method .

from abc import *
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
c.m1()

# Abstract class: sometimes implementation of the class is not complete , such type of partially implementated
# class is known as abstract class .

from abc import *
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

# interface: If an abstract class contains only the abstract method then such type of abstract class is known
# as an interface .

from abc import *
class test :
    @abstractmethod
    def m1(self):pass
    @abstractmethod
    def m2(self):
        pass


class child1(test):
   def m1(self):
       return 100;

   def m2(self):
       print("this is m2 method ")

class parent(test):
    def m1(self):
        return 1000;

c1=child1()
p=parent()
print(c1.m1())
print(c1.m2())
print(p.m1())
print(p.m2())

# __str__() method:whenever we are printing any object reference internally __str__() method is called
# which is returning the string of the following format .
# <__main__.classname object at 0x0454646456>

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
