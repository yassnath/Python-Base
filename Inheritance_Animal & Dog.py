class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def eats(self):
        print(self.name, "is eating...")


class Dog(Animal):
    pass
    
class Cat(Animal):
    pass

spike = Dog("Spike", 5)
print(spike.name)
print(spike.age)
spike.eats()
print(isinstance(spike, Dog))
print(isinstance(spike, Animal))
print(isinstance(spike, Cat))