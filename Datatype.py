
'''#Data types

a=True
b=10.5
c="ten"
print("a")
print(type(a))
print(type(b))
print(type(c))

print("Hello welcome all")
'''

#complex datatype
'''a=10+20j
b=50+100j
print("the addition of a and b is : ",a+b)'''


'''def sum_list(items):
    sum_numbers = 0
    for x in items:
        sum_numbers += x
        return sum_numbers
print(sum_list([1,2,-8]))
'''

'''sun_to_earth=149
sun_to_earth=sun_to_earth+1
print(sun_to_earth)
'''


'''dogsname="tommy"
dogskind="saint bernard"
print("his name is",dogsname,".","he is a",dogskind,".")
'''

'''# 1)list
a=[10,10.5,20,"abc","rohit",10,10.5,"abc"]
a.append("quick xpert")
a.remove(10)
#a.index()
#a.clear()
print(a.count(10))
a.pop(4)
#a.extend(10)
print(type(a))
print(a)
for i in a:
    print(i)'''

'''a=[10,10.5,20,"abc","rohit",10,10.5,"abc"]
index=a.index(20)
print(index)
'''

'''a=[1,5,4,]
#a.append(2)
a.extend([6,1])
print(a)'''


'''g=[1,2,3,4]
for i in g:
    print(i)
'''
'''
k=[4,7,6,2]
k.remove(6)
print(k)'''

'''j=[10,10.5,20,"abc","rohit",10,10.5,"abc","hjk"]
# j.append("aaaa")
# print(j)
# print(j.count(10.5))
#print(j.index("rohit"))
#j.extend("op")
#print(j)
# j.clear()
# print(j)
j.pop()    #removes last item from list
print(j)
for f in j:
    print(f)'''
#####################################################################
'''
#2)Tuple data type

t=(10,20,30,"abc",10.5,"xyz",10)
print(type(t))
print(t)
print(t.count(10))
print(t.index(10))
print(t[::2])
q="quickxpertinfotech.com"
print(q[::])'''

'''g=(11,22,33,44,55,66,77,88)
print(g[0:4:2])
print(g[1:8])
print(g[4:-1])
print(22 in g)
#for data in g:
#    print(data)
'''

'''#range data type
r=range(10,100)
print(type(r))
for i in range(10,100):
    print(i)
'''

'''for i in range(10):
    print(i)

for a in range(0,30,3):
    print(a)
'''

'''for d in range(0,10,2):#
    print(d)'''


'''#byte datatype

x=[10,20,30,40,50,60,70,80,90,100]
b=bytes(x) #byte array
print(type(x))
print(type(b))
print(x)
y=len(b)
print("the lenth is : " ,y)
for i in b:
    print(i)
'''

'''m=[1,2,3,4,5,6,7,8,9,10]
n=bytes(m)
print(type(m))
print(type(n))
c=len(m)
print(c)
for g in n:
    print(g)'''

'''#bytearray
j=[4,5,7,8,9,3,2,1,5]
k=bytearray(j)
print(k)
print(type(j))
print(type(k))
for l in k:
    print(l)'''


'''#set data type mutable
s={10,20,30,"xyz"}
print(type(s))
#s.update("45")
#s.pop()
print(s)
s.add("abc")
print(s)
fs=frozenset(s)
print(type(fs))'''

'''h={'a','b',10,10.5}
fs=frozenset(h)
print(type(h))
print(type(fs))
h.add(55)
h.pop()
print(h)'''

'''people={"akash","ganesh"}
for i in range(1,6):
    people.add(i)
print(people)'''

'''s={1,5,4,6,4,7,8}
print(s)
s.clear()
print(s)'''



'''#dictionary key unique but value can be same
d={10:"abc",20:"def",30:"xyz"}
d1={"abc":10,"def":10,"abc":120}
print(d)
print(d1)
print(d.keys())
print(d.get(10))
print(d.items())
print(d.pop())'''

d={10:"abc",20:"def",30:"xyz"}
# d1={"abc":10,"def":10,"abc":450}
# print(d.keys())
# print(d.get(10))
# print(d.items())
# print(d[20])
#d[10]="null"
#d.clear()
#print(d.pop(10))
print(d)

keys=['ten','twenty','thirty']
values=[10,20,30]
dic1=dict(zip(keys, values))
print(dic1)

'''d2={'name':'jack','age':35}
print(d2.popitem())
d2['name']='maxx'
print(d2)
d2['address']='downtown'
print(d2)
print(d2.items())'''

'''values={1:1, 2:4, 3:9, 5:25}
print(values)
print(values.popitem())
print(values)
#print(values.fromkeys())
'''











































