import json

f = open('data.json')

data = json.loads(f.read())

print(data)

name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")
sex = input("Enter your sex: ")

data_to_save = {
    "name": name,
    "age": age,
    "city": city,
    "sex": sex
}