""" write a program that asks the user to enter three number(use three seperate input statements).
 create a variable called total and avg that hold the sum and avg of the three numbers and printout the values of the total and avg"""
a = int(input("Enter a number:-"))
b = int(input("Enter a number:-"))
c = int(input("Enter a number:-"))
total = a + b +c
avg = total/3
print("The Sum is:-",total,"\nThe average is:-",avg)

#read two number and display their sum
x = int(input("Enter a number:-"))
y = int(input("Enter a number:-"))
sum = a + b
print(sum)
#check the number is even or not
a = int(input("Enter the number:-"))
if a % 2 == 0:
    print("Even")
else:
    print("Odd")

#check the string is palindrom or not ex malayalam

#for loop
for i in range(5):
    print(i)

for i in range(1,11):
    print("7 x",i,"=",7*i)