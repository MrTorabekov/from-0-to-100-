import requests

url = "https://jsonplaceholder.typicode.com/posts"

params = {"userId":1}
headers = {"Authorization":"Bearer mytoken"}  # noqa

# post request
response = requests.get(url,headers=    headers,params=params)


if response.status_code == 200:
    print("data: ")
    print(response.json())
    print("Successful")
elif response.status_code == 201:
    print(f"Error {}")
else:
    print(f"Error : {response.status_code}")