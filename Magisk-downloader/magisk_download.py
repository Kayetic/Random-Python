import requests
import json
import shutil

while True:
    choice = input("""Choose what you would like to download
[1] Magisk (Manager + Recovery Flashable Zip)
[2] LSPosed (Zygisk)
[3] Universal auth files""")

# response = requests.get('https://api.github.com/repos/topjohnwu/Magisk/releases/latest')
response = requests.get('https://api.github.com/repos/LSPosed/LSPosed/releases/latest')
data = response.json()
download_url = data["assets"][1]["browser_download_url"]
print(download_url)


github_response = requests.get(download_url)
text = download_url.split("/")
filename = text[-1]
print(f"Downloading: {filename}")
    
open(filename, "wb").write(github_response.content)
print("Downloaded")
print("\n")

shutil.copyfile(filename, f"./{filename[:-4]}.zip")

temp = input("\nPress ENTER to exit")
exit()
