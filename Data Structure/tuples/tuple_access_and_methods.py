#tuples 
my_tuple = (1, 2, 3, 4, 5)
#accessing elements
print(my_tuple[0]) # 1
print(my_tuple[1:4]) # (2, 3, 4)

#two methods for tuples
#1. count() - returns the number of times a specified value appears in the tuple
my_tuple = (1, 2, 3, 4, 5, 2, 2)
print(my_tuple.count(2)) # 3
#2. index() - returns the index of the first occurrence of a specified value
print(my_tuple.index(2)) # 1
