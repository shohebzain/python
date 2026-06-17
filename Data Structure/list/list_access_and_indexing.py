a = [1,2,3,4,5]
print(a[0]) # 1
print(a[1]) # 2

# first way of acessing list elements
b = [1,2,3,4,5]
for i in range(len(b)):
    print(b[i]) # 1 2 3 4 5
    print(i) # 0 1 2 3 4(index of the list)

# second way of accessing list elements
c = [1,2,3,4,5]
print(c) # [1, 2, 3, 4, 5]

print(dir(c)) # ['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__']