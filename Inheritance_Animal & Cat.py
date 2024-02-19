class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eats(self):
        print(self.name, "is eating...")

class Cat(Animal):
    def __init__(self, name, age, is_heterochromia):
        super().__init__(name, age)
        self.is_heterochromia = is_heterochromia

tom = Cat("Tom", 3, False)
print(tom.is_heterochromia)
print(tom.name)
print(tom.age)
tom.eats()
print(isinstance(tom, Cat))
print(isinstance(tom, Animal))
