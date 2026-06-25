#the two number are close  or not with difference of 0.01
a = float(input("Enter a number:-"))
b = float(input("Enter a number:-"))
if a + 0.01 == b:
    print("a is close to b")
elif b + 0.01 == a:
    print("b is close to a")
else:
    print("Not close")    
