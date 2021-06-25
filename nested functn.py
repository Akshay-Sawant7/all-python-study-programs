#eg 1
'''def outer():
    print("this is outer funtn")
    def inner():
        print("this is inner funtn")
        def innermost():
            print("this is innermost funtn")
        innermost()
    inner()
outer()'''

#eg2
'''def outer():
    print("this is outer funtn")
    def inner():
        print("this is inner funtn")
    inner()
outer()'''

#eg 3

def num1(x):
    def num2(y):
        return  x*y
    return num2
result=num1(10)
print(result(20))



