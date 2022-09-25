import requests
import time


available_names = []

#function to read names from file into array
def read_names():
    names = []
    with open("Name-Sniper/names_to_test.txt") as f:
        for line in f:
            names.append(line.strip())
    return names

names_to_check = read_names()
print(read_names())

def check_username(username):
    request_data = requests.get("https://api.mojang.com/users/profiles/minecraft/" + username)
    if request_data.status_code == 204:
        print("Username " + username + " is available")
        available_names.append(username)
    elif request_data.status_code == 200:
        print("Username " + username + " is taken")

#check if the username is available
for i in range(1300):
    check_username(names_to_check[i])
    time.sleep(0.5)

print("Done\n")
print("Available names: " + str(len(available_names)))
print(available_names)
