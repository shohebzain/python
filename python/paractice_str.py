str1 = input("Enter the string:-")
str2 = input("Enter the string:-")
newstr = " "
if(len(str1) != len(str2)):
    print("sorry! The length is not matching...")
else:
    for i in range(0,len(str1)):
        newstr += str1[i]
        newstr += str2[i]
print(newstr)