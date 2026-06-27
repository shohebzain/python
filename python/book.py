def first_diff(string1, string2):
    str1 = string1.split()
    str2 = string2.split()
    x=" "
    y=" "
    if(len(str1)<len(str2)):
        max_len = len(str2)
    else:
        max_len=len(str1)
        if str1 == str2:
            print("-1")
            exit
    for i in range(max_len):
        if str1[i] != str2[i]:
            x=str1[i]
            y=str2[i]
print("the location of string differs in first string at:",x,"and in second string at:",y)

