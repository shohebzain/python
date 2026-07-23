class Animal:
    name = "lion" # class attribute

    def __init__(self,age):
        self.age =age #instance attribute
    def show(self): #intance method
        print("HELLO")
    @classmethod #class method target to class
    def hello(cls):
        print("HEY")
    @staticmethod
    def static():
        print("HI")
obj = Animal(12)
obj.show() #HELLO
obj.hello() #HEY 
obj.static() #HI
    
