'''l = 10 #global variable
def function1(n):
   # l=5 #local variable
    m=9 #local variable
    global l
    l = l + 45
    print(l, m)
    print(n, "i have printed")

function1("this is me")
#print(m)
'''
#x = 98
def maxx():
    x = 20
    def rohan():
        global x
        x = 77
    print("before calling rohan()", x) #ctl + d
    rohan()
    print("after calling rohan()", x)

maxx()
print(x)

