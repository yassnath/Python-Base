class Car:
    def __init__(self, color): # constructor
        self.color = color # object/instance attribute
        self.is_on = False # object/instance attribute

rez = Car("red")
print(rez.color)
print(rez.is_on)
print(type(rez))

print("=========================")

class Car:
    num_of_wheels = 4 # class attribute
    def __init__(self, color): # constructor
        self.color = color # object/instance attribute
        self.is_on = False # object/instance attribute

rez = Car("red")
benny = Car("orange")
print(rez.color)
print(benny.color)
print(rez.num_of_wheels)
print(benny.num_of_wheels)

print("=========================")

class Car:
    num_of_wheels = 4 # class attribute
    def __init__(self, color): # constructor
        self.color = color # object/instance attribute
        self.is_on = False # object/instance attribute
    def starts(self): # method
        self.is_on = True
        print("Car starts")
    def stops(self): # method
        self.is_on = False
        print("Car stops")

rez = Car("red")
print(rez.is_on)
rez.starts()
print(rez.is_on)
rez.stops()
print(rez.is_on)

