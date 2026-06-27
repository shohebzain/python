d = {10: 20, 30: 40, 50: 60}
d[0] = 70 # adding a new key-value pair to the dictionary
d[10] = 80 # updating the value of an existing key in the dictionary
d.pop(30) # removing a key-value pair from the dictionary using the pop() method
del d[50] # removing a key-value pair from the dictionary using the del statement
print(d) # {10: 80, 0: 70}

#write a python script to merge two dictionaries and print the result
dict1 = {1: 'a', 2: 'b', 3: 'c'}
dict2 = {4: 'd', 5: 'e', 6: 'f'}
merged_dict = {**dict1, **dict2} # merging the two dictionaries using the unpacking operator
print(merged_dict) # {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f'}        

#sum all the values in a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}
total = sum(my_dict.values()) # summing all the values in the dictionary using the values() method
print(total) # 6

#count the frequency on each element in dist
my_list = ['a', 'b', 'c', 'a', 'b', 'a']
frequency = {}
for item in my_list:
    if item in frequency:
        frequency[item] += 1 # incrementing the count of the item in the frequency dictionary
    else:
        frequency[item] = 1 # initializing the count of the item in the frequency dictionary
print(frequency) # {'a': 3, 'b': 2, 'c': 1}

#Write a Python program to combine two dictionary by adding values for common keys.
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}
for key, value in dict2.items():
    if key in dict1:
        dict1[key] += value
    else:
        dict1[key] = value
print(dict1) # {'a': 1, 'b': 6, 'c': 8, 'd': 6}
