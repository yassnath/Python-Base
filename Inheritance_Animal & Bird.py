class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eats(self):
        print(self.name, "is eating...")

class Bird(Animal):
    def __init__(self, name, age, colors):
        self.name = name
        self.age = age
        self.colors = colors

    def colors(self):
        print(self.name, ["Yellow", "White"])
    
    def flies(self):
        print(self.name, "is flying...")

class Cat(Animal):
    pass

class Dog(Animal):
    pass

cuckoo = Bird("Cuckoo", 2, ["Yellow", "White"])
print(cuckoo.colors)
print(cuckoo.name)
print(cuckoo.age)
cuckoo.eats()
cuckoo.flies()
print(isinstance(cuckoo, Bird))
print(isinstance(cuckoo, Animal))
print(isinstance(cuckoo, Cat))
print(isinstance(cuckoo, Dog))