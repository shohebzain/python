#calculate area of a triangle(1/2*base*height)
base = int(input("Enter the base:-"))
height = int(input("Enter the height:-"))
area = 0.5 * base * height
print("The area of the triangle is:", area)

""" write a program that asks the user to enter three number(use three seperate input statements).
 create a variable called total and avg that hold the sum and avg of the three numbers and printout the values of the total and avg"""
a = int(input("Enter a number:-"))
b = int(input("Enter a number:-"))
c = int(input("Enter a number:-"))
total = a + b +c
avg = total/3
print("The Sum is:-",total,"\nThe average is:-,avg")