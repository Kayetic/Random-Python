from textwrap import indent
import requests
import json

response = requests.get('https://api.github.com/repos/topjohnwu/Magisk/releases/latest')
# print(response.json())

print(type(response.json()))
data = response.json()
print(data[0]['url'])