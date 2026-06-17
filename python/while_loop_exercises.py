#seperate each digit of a number and print it on new line.
num = int(input("Enter a number :"))
while num > 0:
    print(num % 10)
    num = num//10

#take the input from the user and extract the digit's
num1 = int(input("Enter the input: "))
rev = 0
while num1 > 0:
    rev = rev *10 + num1 % 10
    num1 = num1 // 10
print(rev)

#check the given number is palindrom or not
num = int(input("Enter the input: "))
copy_num = 0
rev = 0
while num > 0:
    rev = rev *10 + num % 10
    num = num // 10
if copy_num == rev:
    print("palindromic number")
else:
    print("not a palindrone number")

#gussing the randon number
import random
num = random.randint(1,100)
guess = int(input("please guess the number: "))
print(num)
if num == guess:
    print("You are Right!")
else:
    print("Sorry you are wrong")