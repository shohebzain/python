#check the list is sorted or not
a = [1,2,3,4,5] #list
if a == sorted(a):
    print("The list is sorted.")
else:
    print("The list is not sorted.")

#tuple
a = (1,2,3,9,5)
if a == sorted(a):
    print("The tuple is sorted.")
else: 
    print("The tuple is not sorted.")

# to access the elements through the index.
tu = (39,'abc',4.56,(2,3),'def')
print(tu[1])
li =["abc",12,4.32,39]
print(li[1])
#find the highest element in tuple
tuple1 = (1, 2, 3, 4, 5) 
print(max(tuple1))
# the max unicode value element will be the output
a = ("a","A")
print(max(a))
print(min(a))
#sum of the elements of tuple
tuple1 = (1, 2, 3, 4, 5) 
print(sum(tuple1))
#converting the list to tuple and tuple to list 
list1 = [1,2,3,4,4,5,67,4,2]
tuple1 = tuple(list1)
print(tuple1)
# To store the string in list or string is converted in list
s1 = "shoheb"
list2 = list(s1)
print(list2)
