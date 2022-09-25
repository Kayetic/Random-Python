import requests
import random
import string


available_names = []

def check_username(username):
    r = requests.get("https://api.mojang.com/users/profiles/minecraft/" + username)
    if r.status_code == 204:
        print("Username " + username + " is available")
        available_names.append(username)
    elif r.status_code == 200:
        print("Username " + username + " is taken")
    else:
        print("Error: " + r.status_code)

#check if the username is available
# check_username("cat239746")

#define a function to generate a string of random 3 letters



def generate_username():
    username = letter_random_string()
    check_username(username)

def letter_random_string():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(3))


for i in range(999):
    generate_username()

print(available_names)

def write_to_file():
    with open("available_names.txt", "w") as f:
        for name in available_names:
            f.write(name + "\n")

write_to_file()

print("Done")