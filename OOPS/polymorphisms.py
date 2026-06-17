"""def show():
    print("how are you")

def show(): #same name with different methods
    print("you are best")#overwrite the super class 
show()"""

#there are two ways to acheive the polymorphisms
"""class Animal:
    def show(self):
        print("hello iam shoheb")

class human(Animal):
    def show(self):
        print("How are you ")

obj = human()
obj.show()"""

class Apple:
    def show(self):
        print("A")

class Banana:
    def show(self):
        print("B")

obj = Apple()
obj2 = Banana()

obj.show()
obj2.show()