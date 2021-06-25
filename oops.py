'''oops Concept (object Oriented Programming ):-
-----------------------------------------------
5 pillars of OOPs
1)class and Object
2)Inheritance
3)Polymorphism
4)Encapsulation
5)Abstraction
'''

#class & object
'''
class Student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks

    def m1(self):
         print("hello my name is : " , self.name)
         print("hello my age is  : " , self.age)
         print("hello my marks is : " , self .marks)
    def m2(self):
        print("this is 2 nd method")

st=Student("raj",30,50)
st.m1()
st.m2()'''

'''class Demo:
    def __init__(self, name, address):
        print("will execute automatically",name,address)
    def m1(self):
            print("hello to the class concept")
d=Demo("rohit","mumbai")
d.m1()
'''

#self parameter

'''class Stu:
    id=10
    name="rohit"
    def display(selfi):
        print("the id is :%d \n name is :%s"%(selfi.id,selfi.name))
s=Stu()
s.display()
'''

#inheritance

'''class parent:
    def m1(self):
        print("this is a parent method ")

class child(parent) :
    def m2(self):
        print("this is child method ")

c=child()
c.m2()
c.m1()
'''
# 1 simple inheritance
'''
class parent:
    def m1(self):
        print("this is a parent method ")

class child(parent) :
    def m2(self):
        print("this is child methosd ")

c=child()
c.m2()
c.m1()'''

# 2 multi level inheritance
'''
class grandparent:
    def gp(self):
        print("this is grand parent class ")
class parent(grandparent):
    def m1(self):
        print("this is a parent method ")

class child(parent) :
    def m2(self):
        print("this is child methosd ")

c=child()
c.m2()
c.m1()
c.gp()'''

# 3 Hierarchical Inheritance
'''
class parent:
    def p(self):
        print("this is the parent method ")

class child1(parent):
    def c1(self):
        print("this is the child 1 class ")

class child2(parent) :
    def c2(self):
        print("this is rhe child 2 class ")

chl1=child1()
chl1.p()
chl2=child2()'''

# 4 multiple inheritance

'''class Parent():
    def m1(self):
        print("this is parent class method")

class child:
    def m1(self):
        print("this is childclass m2 method")

class Demo(Parent,child):
    def m2(self):
        print("hello")
ch=Demo()

ch.m1()
'''
# 5 cyclic inheritance - not supported in python or any other lang

'''class parent(child):
    def m1(self):
        print("hello ")

class child(parent) :
    def m2(self):
        print("hii")'''

#inheritance sir class practice

'''class Gparent:
    def n0(self):
        print("this is gp class")
class parent(Gparent):
    def n1(self):
        print("this is parent class mothod")

class child(Gparent,parent):
    def n2(self):
        print("this is child class method") ####
c=child()
c.n1()
c.n2()
'''
#cyclic

'''class parent(child):
    def m1(self):
        print("hello ")

class child(parent) :
    def m2(self):
        print("hii")
'''