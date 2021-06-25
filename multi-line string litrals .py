#multi line string literals
# s='''abc
# def'''
# s1="a"
# print(s)
# print(type(s))
# print(type(s1))

'''s=input("enter ur city which u want to visit:")
l1=["Delhi","Mumbai","Pune"]
if s.strip() in l1:
    print("u can travel and book the ticket")
else:
    print("you cant visit this location")
'''

'''s=input("enter the string")
print("characters at even places ",s[::2])
print("characters at odd places ",s[1::2])'''

#functions of string data type
#count()
'''s="absvdghjjhsxxjhskajskxj"
print(s.count("a"))

# replace
s="shhssgshkagshssjs"
print(s.replace("s","p"))

#split()
s="abcdef xyz"
l1=s.split()
print(type(l1))
for x in l1
print(x)

s="abcdef xyz"
l1=s.split("d")
print(l1)

s="bahsg$ndbd"
l1=s.split("$")
print(type(l1))
for x in l1:
    print(x)
'''

#join()
'''l=["abc","def","hjk"]
s="-".join(l)
print(s)'''

#change the cases
'''s="hello how ARE YOU"
print(s.upper())
print(s.lower())
print(s.swapcase())
print(s.title())
'''

#start with(): gives t or f
'''a="hello how R U"
print(a.startswith("hi"))
'''
#ends with
'''a="hello how R you"
print(a.endswith("you"))'''

#isalpha
'''k="agjhfs"
print(k.isalpha())'''

#list
'''k1=[10,20,30,40,50]
print(len(k1))
print(k1.count(10))
print(k1.index(40))
'''
#extend
'''l1=[10,20,30,40]
l2=["abc","xyz","def"]
l1.extend(l2)
l2.extend(l1)
l3=l1+l2
print(l3)'''

l1=[10,20,30,40]
l2=[10,20,30,40,50]
print(l1<l2)


