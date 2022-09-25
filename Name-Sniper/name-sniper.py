import requests
import random
import string

def check_username(username):
    r = requests.get("https://api.mojang.com/users/profiles/minecraft/" + username)
    if r.status_code == 204:
        print("Username " + username + " is available")
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


for i in range(100):
    generate_username()