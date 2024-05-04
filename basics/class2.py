# multiple inheritance

class FirstClass:
    def first_class(self):
        print('first')
        return
    
    def display_name(self):
        print("displaying name from first")
        print(self.name)
        return

class SecondClass:
    def second_class(self):
        print('second')
        return

    def set_name(self, name):
        self.name = name
        return
    
    def display_name(self):
        print("displaying name from second")
        print(self.name)
        return

class ThirdClass (FirstClass, SecondClass):
    def third_class(self):
        print('third')
        return

    # writing to override
    def display_name(self):
        print("displaying name from third")
        print(self.name)
        return

obj = ThirdClass()
obj.first_class()
obj.second_class()
obj.third_class()

# first we setting name
obj.set_name("safeer")

# we are calling display_name method which exists in every class with same name
# so it will override 
# rule is left to right, so if the "display_name()" name method is existing in the third class itself, it will use that
# otherwise check in FirstClass, then SecondClass(left to right as inherited)
obj.display_name()
print(ThirdClass.mro())