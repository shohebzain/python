class Factory:
    a = "Hyderabad"

    def show(self):
        print("this factory in hyderabad")

obj = Factory()
print(obj.a) #accessing the a 
obj.a = "Karimnagar" # a can be change 
# we can access and change the altribute a. To not access and access we have to use encapsulation 
