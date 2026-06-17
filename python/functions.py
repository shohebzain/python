# This is a sample Python script of functions that perform various tasks.
from ast import arguments


def greet():
    print("Hello, World!")
def greeting(name):
    return f"Hello, {name}!"
def add(a, b):
    return a + b
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
print(greet())
print(greeting("Alice"))
print(add(5, 3))    
print(factorial(5))
print(greet())

def hello(name,age):
    print(f"Hello {name}, you are {age} years old.")
hello("Bob", 30) #directly calling the function with arguments
hello(name="Charlie", age=25) #using keyword arguments
hello("Dave", age=40) #mixing positional and keyword arguments
hello(20, "Eve") #incorrect order of arguments, will cause an error

#check the string is palindron or not 
def pallindron(st):
    rev = ""
    for i in range(len(st)-1,-1,-1):
        rev = rev + st[i]
    if st == rev:
        return True
    else:
        return False
print(pallindron("madam"))
print(pallindron("hello"))
print(pallindron("shoheb"))