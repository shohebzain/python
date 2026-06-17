# 1.Accept an interger and print hello world n times.
a = int(input("Enter a number: "))
for i in range(a):
    print("Hello World")

# 2. print natural number upto n
n = int(input("Enter a number: "))
for i in range(1,n+1):
    print(i)
# reverse for the loop. print n to 1
x = [1,2,3,4,5]
for i in range(4,-1,-1):
    print(x[i])
#take a number as input and print the table.
y = int(input("Enter a number: "))
for i in range(y,y*10+1,1):
    print(i)
# sum of n natural numbers
z = int(input("Enter a number: "))
sum = 0
for i in range(0,z+1,1):
    sum += i
    print(sum)
#factorial of a number
fact = int(input("Enter a number: "))
factorial = 1
for i in range(1,fact+1):
    factorial *= i
    print(factorial)
#take the input from the user check the even or odd and add the sum of even and odd numbers separately.
num = int(input("Enter a number: "))
even_sum = 0
odd_sum = 0
for i in range(num+1):
    if i % 2 ==0:
        even_sum += i
    else:
        odd_sum += i
print("The Even sum is: ",even_sum)
print("The Odd sum is: ",odd_sum)
#check whether the number is perfect or not. A perfect number is a positive integer that is equal to the sum of its proper divisors, excluding
f = int(input("Enter a number: "))
sum = 0
for i in range(1,f):
    if f % i == 0:
        sum += i
if sum == f:
    print("The number is perfect")  
else:    
    print("The number is not perfect") 

#check weather the number is prime or not.
f_num = int(input("Enter a number: "))
count = 0
for i in range(1,f_num+1):
    if f_num % i == 0:
        count += 1
        
if count == 2:
    print("The number is prime")
else:
    print("The number is not prime")

#reverse a string using for loop.
a_data = "Shoheb"
b =""
for i in range(len(a_data)-1,-1,-1):
    b = b + a_data[i]
print(b)

#check the palindron or not
a_data = "Shoheb"
b =""
for i in range(len(a_data)-1,-1,-1):
    b = b + a_data[i]
print(b)

if b == a_data:
    print("your string is palindron")
else:
    print("Not a palindron")

#take input (all the datatypes) from the user and print the data type of the input.
    a = "shoheb123!@#"
alpha = 0
digit = 0
special = 0     
for i in a:
        if i.isalpha():
            alpha += 1
            print("The Sum of charector is: ",alpha)
        elif i.isdigit():
            digit += 1
            print("The Sum of digit is: ",digit)
        else:
            special += 1
            print("The Sum of special characters is: ",special)
    
