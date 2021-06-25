'''print("hello", end="")
print("how r u",end="")
print("welcome")'''

'''a=10
b=20
c=30
print(a,b,c,sep="$")'''

a=10
b=20.4
c="abc"
print("a value is %d" %a)
print("b value is %f" %b)
print("c value is %s" %c)

a,b,c=[int(x) for x in input("enter 3 nos").split(",")]
print(a,b,c , sep="$")
