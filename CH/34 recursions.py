# n!=n*n-1*n-2*n-3.......1
# n!=n*(n-1)!
#factorial using iterative method
'''def factorial_iterative(n):
    fac = 1
    for i in range(n):
        fac = fac * (i+1)
    return  fac

number = int(input("Enter the number"))
print("Factoial using itertive method", factorial_iterative(number))'''

#Factoial using recursive method
'''def factorial_recursive(n):
    if n==1:
        return  1

    else:
        return n * factorial_recursive(n-1)
number = int(input("Enter the number"))
print("Factoial using recursive method", factorial_recursive(number))
'''
def fibonacci(n):
    if n==1:
        return  0
    elif n==2:
        return 1
    else:
        return  fibonacci(n-1) + fibonacci(n-2)
number = int(input("Enter the number"))
print(fibonacci(number))















