#eg 1

'''print("this is before exception ")
try:
    print(10/0)
except ArithmeticError:
    print("u are dividing by zero")
print("hello this is after exception")
print("hi")
print("hello")'''

#eg 2

'''try:
    x=int(input("enter first no "))
    y=int(input("enter second no "))
    print(x/y)
except ZeroDivisionError:
    print("you can divide the number with zero")
except ValueError:
    print("enter only numeric digits")
print("thank you for using this app")'''

#eg 3

'''try:
    x=int(input("enter first no "))
    y=int(input("enter second no "))
    print(x/y)
except BaseException as msg:
    print("your problem is ",msg)
print("thank you for using this app")
'''

#eg 4 finally

'''try:
    x=int(input("enter first number"))
    y=int(input("enter second number "))
    print(x/y)
except BaseException as msg:
    print("your problem is ",msg)

finally:

    print("thank you for using this app")
'''

#eg 5

'''try:
    a=int(input("enter first number"))
    b=int(input("enter second number "))
    print(a/b)
except BaseException as msg:
    print("your problem is ",msg)

finally:

    print("good bye.....")
'''
#Nested try- except finally

'''try:
    print("this is first try block")
    try:
     x=int(input("enter first number"))
     y=int(input("enter second number "))
     print(x/y)
    except ZeroDivisionError:
        print("division by zero")
except BaseException as msg:
    print("your problem is ",msg)

finally:

    print("thank you for using this app")
'''
#User Defined / Customized Exception
'''
class userException(Exception):
    def __init__(self,arg):
        self.msg=arg

age=int(input("Enter your age"))
if age>60:
     raise userException  ("you cant register")
else:
     print("registration done")
'''
#practice
# eg reciprocal of given no:
'''import sys
randomlist=['a',0,2]
for entry in randomlist:
    try:
        print("the entry is",entry)
        r = 1/int(entry)
        break
    except:
        print("oops!",sys.exc_info()[0],"occurred")
        print("next entry.")
        print()
print("The reciprocal of", entry, "is", r)
'''
# positive no
'''try:
    a=int(input("enter a positive no: "))
    if a<=0:
        raise ValueError("that is not a positive no!")
except ValueError as ve:
    print(ve)'''

#wap to print reciprocal of even nos

'''try:
    num=int(input("enter a no: "))
    assert num % 2 ==0
except:
    print("not an even no!")
else:
    reciprocal = 1/num
    print(reciprocal)
'''

#finally eg

def divide(x,y):
    try:
        result=x//y
    except ZeroDivisionError:
        print("sorry! you are dividing by zero ")
    else:
        print("yeah! your answer is :",result)
    finally:
        print("this is always executed")
divide(11,3)







