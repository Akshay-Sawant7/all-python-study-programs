#1)array():

'''import numpy as np
arr=np.array([101,102,103,104],int)
print(arr)'''

#neg 1
'''import numpy
arr = numpy.array([1, 2, 3, 4, 5])
print(arr)
'''
#neg 2 numpy as np
'''import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)'''

#checking numpy version
'''import numpy as np
print(np.__version__)
'''

#Create a NumPy ndarray Object:
#neg 3
'''import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))'''

#0-D Arrays
#neg 4

'''import numpy as np
arr = np.array(52)
print(arr)'''

#1-D Arrays
#neg 5
'''import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)'''

#2-D Arrays
#neg 6
'''import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
'''

#3-D arrays
#neg 7

'''import numpy as np
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)'''

#Check Number of Dimensions ?
#neg 8
'''import numpy as np
a = np.array(42)
b = np.array([1,2,3,4,5])
c = np.array([[1,2,3], [4,5,6]])
d = np.array([[1,2,3], [4,5,6],[1,2,3],[4,5,6]])
print("the dimention of the array a is : ",a.ndim)
print("the dimention of the array a is : ",b.ndim)
print("the dimention of the array a is : ",c.ndim)
print("the dimention of the array a is : ",d.ndim)'''

#Higher Dimensional Arrays : Creating an array with 5 dimensions and verify that it has 5 dimensions
#neg 9
'''import numpy as np
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)
'''
#creating the array using linespace()
#neg
'''from numpy import *
arr=linspace(1,8,5,endpoint=False)
for i in arr:
    print(i)
'''

#example with index :-
#neg
'''from numpy import *
arr=linspace(1,8,5,endpoint=False)
n=len(arr)
for i in range(n):
    print(arr[i])
'''
'''from numpy import *
arr=linspace(1,8,5,endpoint=True)
n=len(arr)
for i in range(n):
    print(arr[i])
'''

'''from numpy import *
arr = linspace(1,8,5,endpoint=False)
n=len(arr)
i=0
while i<n:
    print(arr[i])
    i += 1'''

'''from numpy import *
arr = linspace(1, 8, 5, endpoint=True)
n = len(arr)
i = 0
while i < n:
    print(arr[i])
    i += 1'''

'''import numpy
stu_roll=numpy.array([101,102,103,104])
for i in stu_roll:
    print(i)
'''

'''import numpy
stu_roll=numpy.array([101,102,103,104])
n=len(stu_roll)
print(n)
for i in range(n):
    print(stu_roll[i])
    print("index",i,"=",stu_roll[i])'''

'''import numpy
stu_roll=numpy.array([101,102,103,104,105,106])
n=len(stu_roll)
print(n)
i=0

while i<n:
    print("index",i,"=",stu_roll[i])
    i+=1
'''

# using logspace
from numpy import *
arr = logspace(1,8,5,endpoint=False)
n=len(arr)
i=0
while i<n:
    print(arr[i])
    i += 1

#NaN - not a number

