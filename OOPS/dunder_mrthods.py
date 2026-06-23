"""class person:
    def __init__(self, name):
        # store the name for this person object
        self.name = name

# create a person instance
p = person("Ravi")
# print the stored name
print(p.name) #Ravi"""

# Animal class demonstrating dunder methods __str__ and __add__
class Animal:
    def __init__(self,name,age):
        self.name = name  # assign the passed name to the object
        self.age = age

    def __str__(self):
        return "Hello"  # define string representation for the object

    def __add__(self, other):
        return f"sum of ages is {self.age + other.age}"
            
obj = Animal("lion",12)  # create an Animal instance with name lion.
obj2 = Animal("dolphin",14)
print(obj + obj2)  # print the string representation of obj
