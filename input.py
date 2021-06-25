'''a=int(input("enter fst no "))
b=int(input("enter scond no "))
print(a-b)
print(a+b)
'''

'''a=float(input("enter fst no "))
b=float(input("enter scond no "))
print(a+b)
print(a-b)
'''

'''name=input("enter the name ")
add=input("enter city name ")
phone_no=int(input("enter mobile no "))
height=float(input("enter height "))
print(name)
print(add)
print(phone_no)
print(height)'''

'''
m1=float(input("Voice  "))
m2=float(input("Fixed Broadband  "))
m3=float(input("Value Added Services  "))
m4=float(input("Discount  "))
n1=float(input("Arrears  "))
n2=float(input("Credit  "))
n3=float(input("Services Tax**  "))
n4=float(input("W.H.Tax*  "))
n5=float(input("Late Pay Surcharge  "))
m5=m1+m2+m3+m4
n6=n1+n2+n3+n4+n5
o=m5+n6
print("\nBILL SUMMARY")
print("voice :", m1)
print("Fixed Broadband :", m2)
print("Value Added Services :", m3)
print("Discount :", m4)
print("---------------------------------")
print("Total Services Charges :", m5)
print("---------------------------------")
print("Arrears :", n1)
print("Credit :", n2)
print("Services Tax** :", n3)
print("W.H.Tax* :", n4)
print("Late Pay Surcharge :", n5)
print("---------------------------------")
print("Grand Total", o)
print("---------------------------------")'''





'''print("BILL SUMMARY")
m1=float(input("Voice  "))
m2=float(input("Fixed Broadband  "))
m3=float(input("Value Added Services  "))
m4=float(input("Discount  "))
print("voice :", m1)
print("Fixed Broadband :", m2)
print("Value Added Services :", m3)
print("Discount :", m4)
m5=m1+m2+m3+m4
print("---------------------------------")
print("Total Services Charges :", m5)
print("---------------------------------")
n1=float(input("Arrears  "))
n2=float(input("Credit  "))
n3=float(input("Services Tax**  "))
n4=float(input("W.H.Tax*  "))
n5=float(input("Late Pay Surcharge  "))
print("Arrears :", n1)
print("Credit :", n2)
print("Services Tax** :", n3)
print("W.H.Tax* :", n4)
print("Late Pay Surcharge :", n5)
n6=n1+n2+n3+n4+n5
o=m5+n6
print("---------------------------------")
print("Grand Total", o)
print("---------------------------------")
'''

'''a=eval(input("enter some no: "))
print(type(a))
'''

'''a,b,c=[eval(x) for x in input("enter user id, user name, user sal").split(",")]
print(type(a))
print(type(b))
print(type(c))'''


record={}
n=int(input("enter the no. of student "))
i=1
while i<=n:
    name= input("Enter the name of the student ")
    marks =input("Enter % marks of the student ")
    record[name]=marks
    i=i+1
print("-----------------------------------")
print("student name  ", "\t", "% marks ")
for x in record:
    print("\t",x,"\t \t",record[x])





















