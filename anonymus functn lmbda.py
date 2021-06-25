#use lambda
#eg
'''s=lambda n:n*n
print(s(5))
'''
#eg
# s=lambda a,b:a+b
# print(s(40,30))

#eg
'''s=lambda a,b: a if a>b else b
print("the greater of {} and {} is :{}".format(40,450,s(40,450)))'''

#eg
'''double=lambda x:x*2
print(double(4))'''

#eg
'''mylist=[1,3,4,5,6,7,8,9,11,14,18]
newlist=list(filter(lambda x:(x%2==0), mylist))
print(newlist)
'''
#peg
n1=[1,2,3]
n2=[4,5,6]
d=map(lambda n1,n2:n1+n2,n1,n2)
print(list(d))