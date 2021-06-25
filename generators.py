#eg 1
'''l1=(x*x for x in range(100000))
print(l1)
print(type(l1))
'''

#eg 2
'''def gen():
    yield "a"
    yield "b"
    yield "c"
    yield "d"
    yield "e"
g=gen()
for x in g:
    print(x)'''

#eg 3
'''def count(n):
    print("start")
    while(n>0):
        yield n
        n=n-1
values=count(1000000)
for x in values:
    print(x)'''

#eg 4

'''def mygen():
    n=1
    print("this is print first")
    yield n
    n+=1
    print("this is printed second")
    yield n
    n+=1
    print("this is printed at last")
    yield n
print(mygen())
m=mygen()
for x in mygen():
    print(x)'''

#eg 5
def rev_str(mystr):
    length=len(mystr)
    for i in range(length -1,-1,-1):
        yield mystr[i]
for char in rev_str("abcde"):
    print(char)

#peg
def gen():
    yield 1
    yield 2
    yield 3
for x in gen():
    print(x)