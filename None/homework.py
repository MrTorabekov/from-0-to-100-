# 1

# files = open('homework.txt', 'w')
# files.write("Good Morning")
# files.close()

# 2

# with open('homework.txt', 'r') as file:
#     a = file.read()
#     print(a)
# file.close()

# 3

import json

x = {
  "name": "Diyorbek",
  "age": 16,
  "city": "Tashkent"
}

y = json.dumps(x)

print(y)