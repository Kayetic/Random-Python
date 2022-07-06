from signal import signal, SIGINT
import requests
import json
import shutil
import platform
import os

def handler(signal_received, frame):
    # Handling any cleanup here
    print('\nCTRL-C or SIGINT detected. Exiting gracefully...')
    exit(0)

def generate_github_link(repo_url):
    return repo_url.replace("github.com", "api.github.com/repos") + "/releases/latest"

def append_to_file(filename, data_to_write):
    """
    Appending a line to the end of a file
    Parameters: filename (string) - the name of the file to be read
    data_to_write (string) - the line to be appended to the file
    """
    with open(filename, "a+", encoding='utf-8') as file_object:
        file_object.seek(0)
        reading_data = file_object.read(100)
        if len(reading_data) > 0 :
            file_object.write("\n")
        file_object.write(data_to_write)
        file_object.close()

def read_file(filename):
    """
    Opening a file and reading the contents into a variable called 'lines_data'
    Parameters:filename (string) - the name of the file to be read
    """
    with open(filename, 'r', encoding='utf-8') as file:
        lines_data = file.readlines()
        file.close()
    return lines_data

signal(SIGINT, handler)
os.system("cls") if 'Windows' in platform.system() else os.system("clear")
print("""Choose what you would like to download
[1] Magisk (Manager + Recovery Flashable Zip)
[2] LSPosed (Zygisk)
[3] Universal auth files
Saved links:""")
lines = read_file("saved_links.txt")
for i in range(len(lines)):
    split_lines = lines[i].split("|")
    print(f"[{i+4}] {split_lines[0]}")
print("""
[custom] Add custom URL
[exit] Exit""")
choice = input(">>> ")
if choice == "1":
    response = requests.get('https://api.github.com/repos/topjohnwu/Magisk/releases/latest')
    data = response.json()
    download_url = data["assets"][0]["browser_download_url"]
    github_response = requests.get(download_url)
    text = download_url.split("/")
    filename = text[-1]
    print(f"Downloading: {filename}")
        
    open(filename, "wb").write(github_response.content)
    print("\nDownloaded Magisk files")
    print("\n")

    shutil.copyfile(filename, f"./{filename[:-4]}.zip")

    temp = input("\nPress ENTER to exit\n")
    exit()
elif choice == "2":
    response = requests.get('https://api.github.com/repos/LSPosed/LSPosed/releases/latest')
    data = response.json()
    download_url = data["assets"][1]["browser_download_url"]
    github_response = requests.get(download_url)
    text = download_url.split("/")
    filename = text[-1]
    print(f"Downloading: {filename}")

    open(filename, "wb").write(github_response.content)
    print("Downloaded LSPosed")
    temp = input("\nPress ENTER to exit\n")
    exit()
elif choice == "3":
    response = requests.get('https://api.github.com/repos/null-dev/UniversalAuth/releases/latest')
    data = response.json()
    download_url1 = data["assets"][0]["browser_download_url"]
    download_url2 = data["assets"][1]["browser_download_url"]
    github_response1 = requests.get(download_url1)
    github_response2 = requests.get(download_url2)
    text1 = download_url1.split("/")
    text2 = download_url2.split("/")
    filename1 = text1[-1]
    filename2 = text2[-1]
    print(f"Downloading: {filename1}")
    print(f"Downloading: {filename2}")
    open(filename1, "wb").write(github_response1.content)
    open(filename2, "wb").write(github_response2.content)
    print("Downloaded Universal Auth files")
    temp = input("\nPress ENTER to exit\n")
    exit()
elif choice == "custom":
    user_github_url = input("Enter the Github repo URL of the file(s) you would like to download\n: ")
    new_string = generate_github_link(user_github_url)
    print("Downloading...")
    response = requests.get(new_string)
    data = response.json()
    download_url = data["assets"][0]["browser_download_url"]
    github_response = requests.get(download_url)
    text = download_url.split("/")
    filename = text[-1]
    open(filename, "wb").write(github_response.content)
    print(f"Downloaded: {filename}")
    save_choice = input("\nWould you like to save this for later? (y/n)\n: ")
    if save_choice == "y":
        name = input("\nWhat do you want to save the file as (to show in the list)?\n: ")
        data_to_save = name + "|" + new_string
        append_to_file("saved_links.txt", data_to_save)
        print("\nSaved for later")
    temp = input("\nPress ENTER to exit\n")
    exit()
elif choice == "exit":
    exit()
elif int(choice) > 3:
    links = []
    lines = read_file("saved_links.txt")
    for i in range(len(lines)):
        split_lines = lines[i].split("|")
        links.append(split_lines[1].strip())
    print(f"Downloading from: {links[int(choice)-4]}")
    response = requests.get(links[int(choice)-4])
    data = response.json()
    download_url = data["assets"][0]["browser_download_url"]
    github_response = requests.get(download_url)
    text = download_url.split("/")
    filename = text[-1]
    open(filename, "wb").write(github_response.content)
    print(f"Downloaded: {filename}")
    temp = input("\nPress ENTER to exit\n")
    exit()