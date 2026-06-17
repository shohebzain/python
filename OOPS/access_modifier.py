class Factory:
    a = "Hyderabad"

    def show(self):
        print("this factory in hyderabad")
    
class Knr(Factory):
    def show2(self):
         print(super().a)

obj = Knr()
obj.show2()