# create a class Cube
# with instance attribute of length
# and method get_volume

class Cube:
    
    def __init__(self, length): # constructor
        self.length = length # object/instance attribute
        
    def get_volume(self): # method
        return self.length**3
       
x = Cube(2)
print(x.length)
print(x.get_volume())