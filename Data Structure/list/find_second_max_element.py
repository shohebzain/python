#find the second greatest element and print its index too.
a = [1,2,3,4,5]
max_val = max(a)
a.remove(max_val) # remove the greatest element
second_max = max(a) # find the second greatest element
print("Second greatest element:", second_max)
second_max_index = a.index(second_max) # find the index of the second greatest element
print("Index of second greatest element:", second_max_index)
