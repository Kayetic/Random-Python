import time
import requests


available_names = []

def progress_bar(current, total, bar_length=20):
    percent = float(current) * 100 / total
    arrow = '-' * int(percent / 100 * bar_length - 1) + '>'
    spaces = ' ' * (bar_length - len(arrow))

    print('Progress: [%s%s] %d %%' % (arrow, spaces, percent), end='\r')

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



## Main Program
while True:
    option = input("Would you like to check all names in the list or a specific amount? (all/amount): ")
    if option == "all":
        check_all_names(names_to_check, len(names_to_check), 0.5)
        break
    elif option == "amount":
        amount = input("How many names would you like to check?: ")
        delay = input("How long would you like to wait between each request?: ")
        #progress bar
        for i in range(int(amount)):
            progress_bar(i, int(amount) - 1)
            check_username(names_to_check[i])
            time.sleep(float(delay))
        break
    else:
        print("Invalid option")
        temp = input("Press enter to continue")

print("Done\n")
print("Available names: " + str(len(available_names)))
print(available_names)

if len(available_names) > 0:
    print("Would you like to save the available names to a file? (y/n)")
    save = input()
    if save == "y":
        with open("Name-Sniper/available_names.txt", "w", encoding="utf-8") as f:
            for name in available_names:
                f.write(name + "\r")