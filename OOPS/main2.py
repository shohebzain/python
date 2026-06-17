"""class Factory:
    a = 12 #attribute

    def hello(self):
        print("How are you")
    print("hello how are you iam getting initialized")
print(Factory().a)

Factory().hello()"""
class Factory:
    a = 12 #attribute

    def hello(self):
        print("How are you")
obj = Factory()
obj.hello()

