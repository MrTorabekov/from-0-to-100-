import json

# users = {
#     "name":"Diyorbek",
#     "age": 16,
#     "city":"Tashkent",
#     "language": ["UZB","ENG"],
#     "jobs":"Programming",
#     "programming":["Python","go","rust"],
#     "level": "Junior +"
# }
#
# json_obj = json.dumps(users,indent=4)
#
# with open('AboutMe.json','w') as file:
#     file.write(json_obj)


b = [
]
# json_obj = json.dumps(b,indent=4)
with open("users.json",'r') as file:
    data = json.load(file)
    print(data[0]["name"])
    print(data[1]["name"])

