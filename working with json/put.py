import json

import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

data = {
    "title" : "Python HTTP method",
    "body" : "we use HTTP method in the lesson",
    "userID" : 1
}
# post request
response = requests.put(url,json=data)

# Yangi yaratilgan ma'lumotni chop etamiz  # noqa
if response.status_code == 200: # A status code of 201 indicates that the information has been created
    print("Success Update")
    print(response.json())
else:
    print(f"Error : {response.status_code}")