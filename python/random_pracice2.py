import random
i =[]
c = 0
max_count = 0
for j in range(0,100):
    x = random.randint(0,1)
    i.append(x)
for j in i:
    if j == 0:
        c += 1
    else:
        if c>max_count:
            max_count=c
            c=0
print(i)
print("The longest run of zeros:-",max_count)
