
class Dog:
 
    kind = 'canine'
    country = 'China'
 
    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country
 
dog = Dog('Lily', 3, 'Britain')
print(dog.name, dog.age, dog.kind, dog.country) 
print(Dog.country)
