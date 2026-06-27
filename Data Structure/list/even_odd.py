num = [1,2,3,4,5,6,77,8,9]
even = []
odd = []
for i in num:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
print("even elements in list:-",even)
print("odd elements in list:-",odd)
#print the even and odd elements in list seperately.
