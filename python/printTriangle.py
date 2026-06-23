n = int(input("Enter the number of line:-"))
for i in range(1, n):
    print("*" * i)
# write a program to asks the user to enter a word and print out wheather that contains any vowels.
word = input("Enter string")
vowels ="aeiouAEIOU"
for i in word:
    if i in vowels:
        print(i)
    else:
        print("No vowels")

#write a program that uses a for loop to print the numbers 8,11,14,17,...,83,86,89.
for a in range(8,90,3):
    print(a)

for a in range(8,90,3):
    print(a,",",end="")

# write a program that asks the user for their name and how many times to print it.
string = input("Enter yout name:-")
a = int(input("Enter the number how many times to print"))
for i in range(a):
    print(string)