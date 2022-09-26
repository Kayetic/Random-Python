import time
import requests
from english_words import english_words_lower_set

available_names = []

# four_letter_words = [word for word in english_words_lower_set if len(word) == 4]
# with open("Name-Sniper/four_letter_words.txt", "w", encoding="utf-8") as f:
#     for word in four_letter_words:
#         f.write(word + "\n")

def progress_bar(current, total, bar_length=20):
    """
    displays a progress bar
    parameters: current (int) - the current progress
                total (int) - the total progress
                bar_length (int) - the length of the bar
    """
    percent = float(current) * 100 / total
    arrow = '-' * int(percent / 100 * bar_length - 1) + '>'
    spaces = ' ' * (bar_length - len(arrow))

    print('Progress: [%s%s] %d %%' % (arrow, spaces, percent), end='\r')

#function to read names from file into array
def read_names(filename):
    """
    Reads names from file into array
    """
    names = []
    with open(f"Name-Sniper/{filename}", encoding="utf-8") as f:
        for line in f:
            names.append(line.strip())
    return names

names_to_check = read_names("four_letter_words.txt")

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
    for x in range(int(amount)):
        check_username(check_list[x])
        time.sleep(float(delay))



# for i in range(len(english_words_lower_set)):
#     check_all_names(four_letter_words, 10, 0.1)
#     progress_bar(i, len(english_words_lower_set))


## Main Program
while True:
    option = input("Would you like to check all names in the list or a specific amount? (all/amount): ")
    if option == "all":
        for name in names_to_check:
            check_username(name)
            progress_bar(names_to_check.index(name), len(names_to_check))
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
