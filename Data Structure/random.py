import random
randomNO = random.int(1,10)
userguess = int(input("Guess a number:-"))
if randomNO == userguess:
    print("You guess is correct")
else:
    print("your guess is wrong")
print("The random number is:-",randomNO) 
