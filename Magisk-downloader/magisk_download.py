import requests
import json
import shutil
import platform
import os

os.system("cls") if 'Windows' in platform.system() else os.system("clear")
choice = input("""Choose what you would like to download
[1] Magisk (Manager + Recovery Flashable Zip)
[2] LSPosed (Zygisk)
[3] Universal auth files
[exit] Exit
>>> """)
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
