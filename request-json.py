import requests
import json

url = "https://jsonplaceholder.typicode.com/posts"

r = requests.get(url).json()

for object in r:
    print(object["userId"])