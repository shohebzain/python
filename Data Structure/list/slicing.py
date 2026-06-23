a = "SHOHEB"
print(a[1:4]) #the index start from the 1 and end at 3
print(a[1:-1]) 
print(a[0:])
print(a[:])
print(a)
"""output 
HOH
HOHE
SHOHEB
SHOHEB
"""
tu = (39,'abc',4.56,(2,3),'def')
t1 = tu[1:4:2] #[start,end,steps]
print(t1) #output abc , (2,3)

s = "python"
print(s[::2]) #output pto

s = "python"
print(s[::-1]) #output reverse the string is nohtyp

#To check the element is palindrom or not
text = input("Enter the string:-")
rev = text[::-1]
if text == rev:
    print("String is palindrome")
else:
    print("String is not a palindrome")


# in operator
a = "SHOHEB" 
"s" in a
"SH" in a # is the same sequence output is true else return false
"HS" in a #output is false
print(a.lower())


#UPPERCASE 
a = "shoheb"
print(a.upper()) #SHOHEB
print(len(a))

