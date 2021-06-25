'''def factorial(n):
    result=1
    if n==0:
        result=1
    else:
        result=n*(factorial(n-1))
    return result
print(factorial(4))
'''

def sum(n):
    if n==0:
        return 0
    else:
        return n + sum(n-1)
print(sum(4))    #4+3+2+1=10