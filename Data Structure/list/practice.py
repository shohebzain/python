#write a program that remove the any repeated items from the list. list : [1,1,2,3,4,,3,0,0]
print("Enter the list duplicate values:-")
n = int(input("Enter the number of items:-"))
x = []
y = []
for i in range(0,n):
    element = int(input("Enter the number:-"))
    x.append(element)
print(x)
for j in x:
    if j not in y:
        y.append(j)
print(y)
