#break
#eg 1
'''for i in range(10):
    if i==7:
        print("hello how r u")
        break
    print(i)'''

#eg 2
'''c=[10,20,30,90,40,50,60,70]
for items in c:
    if items >80:
        print("sorry ")
        break
    print("the processed item is ", items)'''

#continue
'''for i in range(10):
    if i%2==0:
        continue
    print("value of i is", i)'''

#pass
#Eg 1
'''if True:
    print("hello")
else:
    print("hi")'''

'''if True : pass
else:
    print("hi")
print("this is pass statement")
'''
#del statement
#eg 1
'''x=45
print(x)
del x
print(x)'''

#eg 2
'''d="fgh"
print(d)
del d[0]
print(d)'''

#none statement
x=10
y=20
del x
y=None
print(y)