'''a=10
def f1():
    global a
    a=20
    print("the value of a in f1 is :",a)
def f2():
    global a
    a = 30
    print("the value of a in f2 is :", a)
def f3():
    print("the value of a in f3 is :",a)
def f4():
    print("the value of a in f3 is :",a)
f1()
f2()
f3()
f4()

'''

'''a=50
def f1():
    global a
    a=100
    print(a)
def f2():
    global a
    print(a)
def f3():
    global a
    a=500
    print(a)
f1()
f2()
f3()'''

#global var eg 1
'''x="global"
def fun():
    print("x inside:",x)

fun()
print("x outside:",x)'''

#eg 2
'''x="global"
def funct():
    global x
    x=x*4
    print(x)
funct()
'''
#local var eg 1
'''def fun():
    y="local"
    print(y)
fun()'''

def sum(x,y):
    sum=x+y
    return sum
print(sum(45,55))


#local global var eg
'''x=5
def fun():
    x=10
    print("local x:", x)
fun()
print("global x:", x)
'''












