'''

#Various properties/attribute of the file : -
f = open("abcd.txt", "w")
print("File name ", f.name)
print("file mode ", f.mode)
print("Is file readable or not  : ", f.readable())
print("Is my file Writable or not : ", f.writable())
print(" is my file closed or not : ", f.closed)
f.close()
print("again plz check whether file closed or not : ", f.closed)

#Example using write () : -
f=open("abcd.txt" , 'w')
f.write("welcome to the write function ")
print("data written successfully")

#Example using the writelines():-
f=open("abcd.txt" , 'w')
list=["abcd ","def ","lmn ","xyz "]
f.writelines(list)
print("data written successfully")
f.close()

'''

#Example using read ():
'''f=open("abcd.txt",'r')
data = f.read()
print(data)
f.close()'''


'''f=open("abcd.txt", 'w')
f.write("welcome to the write function")
f.write("\nmy name is ak")
print("data written successfully")
'''

#Example using Read(n) :
'''f=open("abcd.txt",'r')
data = f.read(5)
print(data)
f.close()'''

#Example using readline():
'''f=open("abcd.txt",'r')
line1=f.readline()
print(line1,end="")
line2=f.readline()
print(line2)'''

#Example using readlines ():
'''f=open("abcd.txt",'r')
line=f.readlines()
for l in line:
    print(l, end="")'''

#How to check a particular file exit or not ?

import os,sys
fname=input("enter file name : ")
if os.path.isfile(fname):
    print("File is there : " , fname)
    f=open(fname,"r")

else:
    print("file not found : " , fname)
    sys.exit()

print("the content of the file is :  ")
data=f.read()
print(data)



























