a = int(input("Enter a number: "))
try:
    result = 10 / a
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

b = int(input("Enter the number"))
try:
    result = 10 / b
    print("result:",result)
except Exception as err:#
    print("Sorry there is a exception:")
else:
    print("Good there is no exception")
finally:
    print("i will run no matter what")