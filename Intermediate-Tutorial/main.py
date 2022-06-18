import time

class Person:

    amount = 0

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
        Person.amount += 1

    def myfunc(self):
        print("Hello my name is " + self.name)

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Height: {self.height}cm"


class Worker(Person):

    def __init__(self, name, age, height, salary):
        super(Worker, self).__init__(name, age, height)
        self.salary = salary
    
    def calculate_yearly_salary(self):
        return self.salary * 12
    def __str__(self):
        return super().__str__() + f", Salary: {self.salary}"

person1 = Worker("John", 30, 175, 2000)
person2 = Worker("Jane", 25, 165, 2500)
