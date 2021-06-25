f=open("ak.txt")
# print(f.tell())
print(f.readline())
# print(f.tell())
f.seek(14) #file ko kahan se padhna start kare isliye seek use
print(f.readline())
# print(f.tell())
f.close()
