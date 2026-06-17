print("Hello, World!")
#This is a simple python script that prints "Hello, World!" to the console. You can run this script in any Python environment to see the output.
""""hello
this 
is a multi-line commentin Python
"""
shoheb = "This is a variable named shoheb"
print(shoheb)
# naming conventions in Python
Shoheb = "This is a variable named Shoheb with capital S"# pascal case naming convention
print(Shoheb)
shoheb = "This is a variable named shoheb with lowercase s"# camel case naming convention
print(shoheb)
Shoheb_a = "This is a variable named Shoheb_a with underscore"# snake case naming convention
print(Shoheb_a)
#data types in Python
a = 39 # integer data type
b = 3.14 # float data type
c = "Hello, World!" # string data type
d = True # boolean data type
e = None # None data type
f = 39j # complex data type
g = True # boolean data type
print(a)
print(b)    
print(c)
print(d)
print(e)
print(f)
print(g)
list1 = [1, 2, 3, 4, 5] # list data type
tuple1 = (1, 2, 3, 4, 5) # tuple data type
set1 = {1, 2, 3, 4, 5} # set data type
dict1 = {"name": "Shoheb", "age": 25, "city": "Dhaka"} # dictionary data type
print(list1)    
print(tuple1)
print(set1)
print(dict1)
#how strings work in Python
a = "A"
print(ord(a)) # ord() function returns the Unicode code point of a given character
chr_value = 65
print(chr(chr_value)) # chr() function returns the character that corresponds to a given Unicode code point   
#String indexing
a = "SHOHEB"
print(a[1]) # String indexing starts from 0, so a[0] returns the first character 'S'
print(a[-1]) # Negative indexing starts from the end of the string, so a[-1] returns the last character 'B'
print(a[-2]) # This will return the last character 'B' as a substring
#String slicing
a = "SHOHEB"
print(a[1:4]) # This will return the substring 'HOH' from index 1 to index 3 (4 is exclusive)
print(a[:4]) # This will return the substring 'SHOH' from the beginning of the string to index 3 (4 is exclusive)
print(a[1:]) # This will return the substring 'HOHEB' from index 1 to the end of the string
print(a[:]) # This will return the entire string 'SHOHEB'
#type conversion in Python
a = 39 # integer data type
b = 3.14 # float data type
c = "Hello, World!" # string data type
d = True # boolean data type    
e = None # None data type
f = 39j # complex data type
g = True # boolean data type
print(float(a)) # This will convert the integer 39 to a float 39.0  
print(int(b)) # This will convert the float 3.14 to an integer 3 (truncating the decimal part)
print(str(c)) # This will convert the string "Hello, World!" to a string (it remains unchanged)
print(bool(d)) # This will convert the boolean True to a boolean (it remains unchanged) 
print(bool(e)) # This will convert the None value to a boolean False
print(complex(a)) # This will convert the integer 39 to a complex number (39+0j)
print(bool(g)) # This will convert the boolean True to a boolean (it remains unchanged)