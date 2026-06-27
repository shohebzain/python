#rotate elements of a list. left rotation by 2
num = [1,2,3,4,5]
rotate = num[2:] + num[:2]
print(rotate)