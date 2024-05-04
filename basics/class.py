class SampleClass:
    # class variable/attribute;
    current_year = 2024

    # constructor
    def __init__(self):
        print("instance created")
        
    # custom function
    def set_name(self, name):
        self.name = name
        return

    # custom function2
    def get_name(self):
        print("its from parentclass")
        print(self.name)
        return
    
    @classmethod
    def increment_year(cls):
        cls.current_year = cls.current_year+1
        return


# creating an object for the class "SampleClass"
obj = SampleClass()
obj.set_name("safeerep")

# the following two have same effect;
obj.get_name()
SampleClass.get_name(obj)

# to see the class attribute
print(SampleClass.current_year)

# calling class method to increment the year;
SampleClass.increment_year()
# printing the year after incrementing;
print(SampleClass.current_year)

# creating new class to inherit SampleClass
class SubClass (SampleClass):
    def __init__(self):
        # when an instance is creating for this class, it will print
        print("instance created for subclass")
        # at the same time, calling parent class' constructor;
        super().__init__()

    # writing get_name method in the same name to override the parent class method
    def get_name(self):
        print("its from subclass")
        print(self.name)
        return


# creating object from/for Subclass
obj2 = SubClass()
# calling SampleClass' method from the Subclass' instance;
obj2.set_name("ep....")
obj2.get_name()