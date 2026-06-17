class Factory:
    def __init__(self, material,zips,pockets): #initialization function in that first accepting the self parameter by putting , ask material zips and pockets
        self.material = material
        self.zips = zips
        self.pockets = pockets

reebok = Factory("leather",2,3)
campus = Factory("nylon",3,3)
print(reebok.pockets) #3
print(reebok) #<__main__.Factory object at 0x0000021D59F37230>