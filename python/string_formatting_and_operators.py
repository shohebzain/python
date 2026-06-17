#input and output
name = "Shoheb"
print("my name is ",name)
age = 25
print("my age is ",age)
print("my name is {} and my age is {}".format(name,age)) # using format() method for string formatting
print(f"my name is {name} and my age is {age}") # using f-strings for string formatting
print("my name is",name,"and my age is",age) # using comma to separate values in print() function


#operators in Python
a = 10
b = 5
# arithmetic operators
print(a + b) # addition operator
print(a - b) # subtraction operator
print(a * b) # multiplication operator
print(a / b) # division operator
print(a % b) # modulus operator
print(a ** b) # exponentiation operator
print(a // b) # floor division operator
# comparison operators
print(a == b) # equality operator
print(a != b) # inequality operator
print(a > b) # greater than operator
print(a < b) # less than operator
print(a >= b) # greater than or equal to operator
print(a <= b) # less than or equal to operator
#assignment operators
a += b # addition assignment operator
a -= b # subtraction assignment operator
a *= b # multiplication assignment operator
a /= b # division assignment operator
a %= b # modulus assignment operator
a **= b # exponentiation assignment operator
a //= b # floor division assignment operator
#logical operator
a = True
b = False
print(a and b) # logical AND operator
print(a or b) # logical OR operator 
print(not a) # logical NOT operator
#conditional statements
x = 10
if x > 0:
    print("x is positive")  
elif x < 0:
    print("x is negative")
else:   
    print("x is zero")
