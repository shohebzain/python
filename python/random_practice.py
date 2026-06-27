""" write a program to generate a list pf 20 random umber between 1 and 100
a) print the list
b) print the average of the elements in the list
c) print the largest and second largest value in list
d) print the second largest and second smallest entries in the list
e) print how many numbers in the list """

import random
list1 = []
n = int(input("Enter the numbers:-"))
for i in range(20):
    list1.append(random.randint(1,100))
print("Random number list is:-",list1)
print("avg of the list of elements:-",round(sum(list1)/len(list1),2)) # 2 means second decimal stops 39.3939 -> 39.39
list1.sort()
print("Largest elements is:-,list[len(list1)]-1")
print("Smallest elements is:-",list1[0])
print("Second largest elements is:-",list1[len(list1)-1])
print("Second smallest is:-",list1[1])
count = 0
for j in list1:
    if j%2==0:
        count += 1
print("No of even numbers in the list:-", count)


