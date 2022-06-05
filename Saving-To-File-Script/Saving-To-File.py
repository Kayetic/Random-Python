import json

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

def save_data(data):
    with open("data.json", "a+") as f:
        json.dump(data, f, indent=4)


save_data(data_to_save)