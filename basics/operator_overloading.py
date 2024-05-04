class FrameNames:
    def set_name(self, name):
        self.name = name
        return 
    
    def get_name(self):
        print(self.name)
        return
    
    # if any objects are using + symbol to add with any other objects this method will be called
    def __add__(self, other):
        print("add method called")
        return self.name +" "+ other.name
    
obj1 = FrameNames()
obj1.set_name("safeer")
obj2 = FrameNames()
obj2.set_name("ep")
obj3 = obj1+obj2
print(obj3)