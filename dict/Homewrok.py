# 1)

# grade = {
#     "math":5,
#     "english": 4,
#     "python": 6,
# }
# print(grade)
# grade["math"] = 4
# print(grade)

# 2)

# user ={
#     "math": 5,
#     "english": 4,
#     "python": 5
#
# }
#
# print(user)
# user["ona tili"] = 2
# print(user)

# 3)

# user = {
#     "name": "Diyorbek",
#     "first_name": "Torabekov",
#     "age": 16
# }
# print(user.items())


# 4)

# users = {
#     "name":"Diyorbek",
#     "Surname":"Diyorbek"
# }
# print(users["Surname"] == users["name"])


# 1)

# movie = {
#     "forsag": "faster",
#     "Taxi 4": "Speed",
#     "Marvel": "fighter"
# }
# print(movie)

# 2)

# movie = {
#     "forsage": "faster",
#     "Taxi 4": "Speed",
#     "Marvel": "fighter"
# }
# print(movie.get('forsage'))
# print(movie.get('Taxi 4'))
# print(movie.get('Marvel'))


# 3)

# movie = {
#     "forsag": "faster",
#     "Taxi 4": "Speed",
#     "Marvel": "fighter"}
# movie.setdefault("language","Uzbek")
# print(movie)

# 4)

# movie = {
#     "forsag": "faster",
#     "Taxi 4": "Speed",
#     "Marvel": "fighter"}
# movie.setdefault("language","Uzbek")
# film = movie.copy()
# movie.clear()
# print(film)

# 5)

# movie = {
#     "forsag": "faster",
#     "Taxi 4": "Speed",
#     "Marvel": "fighter"}
# movie.setdefault("language","Uzbek")
# movie.pop('Marvel')
# print(movie)


# 6)

# movie = {
#     "forsag": "faster",
#     "Taxi 4": "Speed",
#     "Marvel": "fighter"}
# movie.setdefault("language","Uzbek")
# movie.popitem()
# print(movie)

# 7)

# movie = {
#     "forsag": "faster",
#     "Taxi 4": "Speed",
#     "Marvel": "fighter"}
# movie.setdefault("language","Uzbek")
# movie.clear()
# print(movie)