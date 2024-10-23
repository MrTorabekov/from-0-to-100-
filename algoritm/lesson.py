import requests

# Url manzili  # noqa
url = "https://jsonplaceholder.typicode.com/posts"

#  GET so'rob yuboramiz  # noqa
response = requests.get(url)

# Status kodini tekshiramiz # noqa
if response.status_code == 200:
    data = response.json()
    print(data)

else:
    print(f"Error{response.status_code}")