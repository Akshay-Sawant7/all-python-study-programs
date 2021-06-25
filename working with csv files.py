'''import csv
with open("emp.csv","w",newline="")as f:
    w=csv.writer(f)
    w.writerow(["ENo","EName","ESal","EAddress"])
    n=int(input("plz Enter The no of Employees "))
    for i in range(n):
        eno=input("enter employye no : ")
        ename= input("enter employye name :")
        esal= input("enter the salary : ")
        eadd= input("enter the address :")
        w.writerow([eno,ename,esal,eadd])
print("data Written sucessfully in my csv file ")
'''

'''import csv
f=open("emp.csv","r")
r=csv.reader(f)
data=list(r)
for da in data:
    for ja in da :
        print(ja,"\t",end="")
    print()'''

#for read operation
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
