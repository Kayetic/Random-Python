class Person:

    amount = 0

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person.amount += 1
    def __str__(self):
        return f"{self.name} is {self.age} years old and {self.height}cm tall."


person1 = Person("John", 20, 170)
person2 = Person("Jane", 21, 160)
person3 = Person("Jack", 22, 150)

print(person1)
print(person2)
print(person3)
