#merge two list and remove duplicates
l1 = [1,2,23,23,23,2]
l2 = [1,5,3,8,8,5,67]
result = list(set(l1 + l2))
print(result)