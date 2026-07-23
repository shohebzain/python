#simple inheritance
class Factory: #parent class / super class
    a = "iam an attritube mentioned inside factory"
    def hello(self):
        print("hello iam a mthod mentioned inside factory")

class Factoryhyd(Factory): #child class / sub class.
    pass

obj2 = Factoryhyd()
print(obj2.hello()) 
 
