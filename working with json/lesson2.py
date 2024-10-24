import json

import requests

url = "https://jsonplaceholder.typicode.com/posts"

# response = requests.get(url)
#
# if response.status_code == 200:
#     # Javobni json formatda olish  # noqa
#     data = response.json()
#     with open("posts.json","w") as file:
#         file.write(json.dumps(data,indent=4))
#         print("Success")
# else:
#     print(f"Error: {response.status_code}")


# ========================================================================

data = {
    "title" : "Python HTTP method",
    "body" : "we are use HTTP method in the lesson",
    "userID" : 1
}

response = requests.post(url,data)

if response.status_code == 201:
    print("Success created")
    print(response.json())

else:
    print(f"Error : {response.status_code}")