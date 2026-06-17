#print positive and negative numbers in a list
a = [1, -2, 3, -4, 5]
positive = []
negative = []
for num in a:
    if num > 0:
        positive.append(num)
    else:
        negative.append(num)
print("Positive numbers:", positive) # [1, 3, 5]
print("Negative numbers:", negative) # [-2, -4]