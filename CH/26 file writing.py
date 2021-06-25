f = open(("ak.txt"))
print(f.readlines()) #it stores  file data in list
# print(f.readline())
# print(f.readline())
# print(f.readline())
# f = open(("ak.txt", "r")) # open functn 2nd argument is r - read mode
# f = open(("ak.txt", "tb")) #reads in binary string
# f = open(("ak.txt", "rt")) #default mode
content=f.read()
# for line in f:
#     print(line, end="") #print line by line
print(content)
# content=f.read(25)
# print("1", content)
#
# content=f.read(25)
# print("2", content)
f.close()