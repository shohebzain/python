#check wheather two strings are anagrams
a = input("Enter the string:-").lower() #use upper() or lower()
b = input("Enter the string:-").lower()
if sorted(a) == sorted(b):
    print("The string is Anagram")
else:
    print("The string is not a Anagram")
#An anagram is a word or phrase formed by rearranging the letters of another word or phrase using all the original letters exactly once

#word count in a sentence
sentence = input("Enter a sentence:-")
print("Number of words",len(sentence.split()))