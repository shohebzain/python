#find the charectot frequency in a string
text = "shoheb"
frequency ={}
for ch in text:
    frequency[ch] = frequency.get(ch,0)+1
print(frequency)
