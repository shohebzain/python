"""" write a program to ask the user to enter the length of feet. then give the options to user to convert into inches, yards,miles,milimeters,
centimeter"""


feet = int(input("Enter the length of feet:-"))
print(""" choose 1 to convert into inches,choose 2 to convert into yards,choose 3 to convert into miles,choose 4 to convert into milimeters,choose 5 to convert into centimeter,
      choose 6 to convert into meter,choose 7 to convert into kilometer""")
choice = int(input("Enter your choice:-(1-7)"))
if choice == 1:
    result = feet * 12
    print("The inches is:-",result)
elif choice == 2:
    result = feet/3
    print("The yards is:-",result)
elif choice == 3:
    result = feet/5280
    print("The miles is:-",result)
elif choice == 4:
    result = feet*304.8
    print("The milimeters is:-",result)
elif choice == 5:
    result = feet*30.48
    print("The centimeters is:-",result)
elif choice == 6:
    result = feet*0.3048
    print("The meter is:-",result)
elif choice == 7:
    result = feet*0.0003048
    print("The kilometer is:-",result)
else:
    print("Please select the valid option",)