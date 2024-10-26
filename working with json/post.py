import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title":"Python HTTP method",
    "body":"we are use HTTP method in the lesson",
    "userID": 1
}
# post request
response = requests.post(url,data)

# Yangi yaratilgan ma'lumotni chop etamiz
if response.status_code == 201: # A status code of 201 indicates that the information has been created
    print("Success created")
    print(response.json())

else:
    print(f"Error : {response.status_code}")