def originalfunction():
    print("this is function aliasing")
duplicatefunction=originalfunction()
print(id(originalfunction()))
print(id(duplicatefunction))
originalfunction("abc")
duplicatefunction("def")

def first():
    print("this is function aliasing")
second=first()
print(id(first()))
print(id(second))
first("abc")
second("def")
