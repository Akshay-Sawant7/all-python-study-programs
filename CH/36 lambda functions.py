#Lambda or anonymous functions
# def add(a,b):
#     return a+b
'''
#1 use of lambda functn
minus = lambda x, y: x-y

#same as 1
def minus(x, y):
    return  x-y'''

'''def a_first(a):
    return a[1]

a =[[1,14], [5,6], [8,25]]
a.sort(key=a_first)
print(a)'''

a =[[1,14], [5,6], [8,25]]
a.sort(key=lambda x:x[1])
print(a)


