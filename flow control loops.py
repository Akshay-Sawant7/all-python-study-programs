'''a=int(input("enter first no : "))
b=int(input("enter second no : "))
c=int(input("enter third no : "))
d=int(input("enter fourth no : "))
if((a>b) & (b>c) & (c>d) ):
    print("first no is greater")
elif(b>c):
    print("second no is greater")
elif(c>d):
    print("third no is greater")
else:
    print("fourth no is greater")

'''

'''n1 = int(input("enter 1st no"))
n2 = int(input("enter 2nd no"))
if n1 > n2:
    print("bigger no is", n1)
else:
    print("bigger no is", n2)
'''
#for loop
#eg 1
'''s="quickxpert"
for x in s:
    print(x)'''

#eg 2
'''s="abcd"
count = 0
for x in s:
    count +=1
    print(x)
    print("no of characters is", count)'''

#eg 3
'''s="abcdefghijklmn"
count=0
for x in s:
    count +=1
    print(x)
print("no of characters is", count)
print(s)
print(type(x))
print(type(count))'''

#eg 4
'''for x in range(22):
    print("hello")
    print(x)'''

#eg 5
'''r=range(10)
print(type(r))
print(r)

for i in r:
    print(i)'''


#eg 6
'''for x in range(21):
    if x%2 ==0:
        print(x)'''

#eg 7
'''for x in range(5,21,2):
    print(x)'''

#eg 8
'''numbers=[6,4,7,8,2,5,9,8]
sum=0
for val in numbers:
    sum=sum+val
print("the sum is", sum)  '''

#eg 9 iterate list using indexing
'''items=['pop', 'rock', 'jazz']
for i in range(len(items)):
    print("i like", items[i])'''

#eg 10
'''student_name='mangesh'
marks={'james':90, 'jules':65, 'athur':85, 'kaddy':89}
for student in marks:
    if student==student_name:
        print(marks[student])
        break
else:
  print("no entry with this name found")'''

#eg 11 squares pf nos of list
'''nos=[1,2,4,6,7,9,12,14,19]
sq=0
for val in nos:
    sq= val * val
    print(sq)'''

#eg 12 print sum of given range
'''sum=0
for val in range(1,7):
    sum=sum+val
print(sum)'''

#eg 13 for loop else block
'''for val in range(8):
    print(val)
else:
    print("the loop is completed")'''

#14 nested for loop
'''for num1 in range(3):
    for num2 in range(10,14):
        print(num1,",",num2)'''


#while loop
#eg 1 sum of given nos
'''n=int(input("enter no"))
sum=0
i=1
while i <=n:
    sum=sum+i
    i+=1
print("the sum of first",n,"no is ",sum)
'''
#eg 2 username & password
'''username=""

password=""
while username !="abc" or password!="xyz":
    username=input("enter username ")
    password=input("enter password ")
print("hello u r welcomed ")'''

# eg 3 infinite loop
'''i=0
while True:
    i=i+1
    print("hello ", i )'''

#eg 4 to illustrate the use of else statement with while loop
'''counter = 0
while counter<5:
    print("Inside loop")
    counter=counter+1
else:
    print("Inside else")'''

#eg 5 use of break statement
'''i=1
while i<8:
    print(i)
    if i==3:
     break
    i+=1
'''

#eg 6 use of continue statement
'''i=0
while i<8:
    i+=1                      
    if i==3:
      continue
    print(i)'''

#eg 7 print a msg when condtn get false
'''n=int(input("enter a no: "))
i=1
while i<n:
    print(i)
    i+=1
else:
    print("i is no longer less than",n)
'''

#eg 8
'''count=0
while (count < 8):
    print("the count is: ", count)
    count=count+1
print("good buy!")'''

# eg 9 infinite loop
'''var = 1
while var ==1:
    num=int(input("enter a no :"))
    print("you entered: ",num)
print("good buy")'''

# eg 10 infinite loop
'''flag=1
while (flag):
    print("given flag is really true")
print("good buy")
'''
#eg 10

n=int(input("enter a no: "))
i=1
while i<n:
    print(i)
    i+=1
else:
    print("i is no longer less than",n)



















