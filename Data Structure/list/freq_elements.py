num = [1,2,3,4,2,3,2,3,44,34,4,5,6,39,3,434,35,3]
frequency = {}
for i in num:
    if i in frequency:
        frequency[i] += 1
    else:
        frequency[i] = 1
print(frequency)
#find the frequency of each element in the list...
