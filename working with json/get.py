import json
import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

if response.status_code == 200:
    # Get response in json format    data = response.json()
    with open("posts.json","w") as file:
        file.write(json.dumps(data,indent=4))
        print("Success")
else:
    print(f"Error: {response.status_code}")