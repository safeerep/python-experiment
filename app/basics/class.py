class SampleClass:
    def set_name(self, name):
        self.name = name

    def get_name(self):
        print(self.name)
        return
    
# creating an object for the class "SampleClass"
obj = SampleClass()
obj.set_name("safeerep")

# the following two have same effect;
obj.get_name()
SampleClass.get_name(obj)