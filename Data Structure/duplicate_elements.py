#find duplicate elements in a tuple
t = (1,39,2,3,43,2,4,3,2,123,2343,2332,3,323,43)
duplicates = []
for i in t:
    if t.count(i)>1 and i not in duplicates:
        duplicates.append(i)
print(duplicates)