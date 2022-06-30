import requests
import json
import shutil

response = requests.get('https://api.github.com/repos/topjohnwu/Magisk/releases/latest')
data = response.json()
download_url = data["assets"][0]["browser_download_url"]

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
