import requests
import time


available_names = []

#function to read names from file into array
def read_names():
    """
    Reads names from file into array
    """
    names = []
    with open("Name-Sniper/names_to_test.txt", encoding="utf-8") as f:
        for line in f:
            names.append(line.strip())
    return names

names_to_check = read_names()
print(read_names())

def check_username(username):
    """
    Sends a request to the minecraft api to check if a username available
    parameters: username (string) - the username to check
    """
    request_data = requests.get("https://api.mojang.com/users/profiles/minecraft/" + username)
    if request_data.status_code == 204:
        available_names.append(username)
        return True
    elif request_data.status_code == 200:
        return False

def check_all_names(check_list, amount, delay):
    """
    Will check all names in the list and print the available ones
    parameters: check_list (list) - the list of names to check
                amount (int) - the amount of names to check
                delay (int) - the delay between each request
    """
    for i in range(int(amount)):
        check_username(check_list[i])
        time.sleep(float(delay))

print("Done\n")
print("Available names: " + str(len(available_names)))
print(available_names)
