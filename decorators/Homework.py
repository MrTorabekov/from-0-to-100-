import json

s = """
School management system
1.Login
2.Register
3.All users
"""

users = {
    "students": {
        "1": {
            "fullname": "jack",
            "username": "jacks",
            "password": 1111,
            "grade": 4,
            "lesson": "Python,Math,English",
            "class": "10b23",
            "homeTask": "Decorators"
        },
        "2": {
            "fullname": "Diyorbek",
            "username": "Torabekov_08",
            "password": 2222,
            "grade": 5,
            "lesson": "Python",
            "class": "10b23",
            "homeTask": "Decorators"
        },

    }
}

d = """
1. my profile
2. my lesson
3. my class
4. homeTask
5. Break
"""

# data types for while

while 1:

    e = str(input(f"{s}"
                  f":"))
    if e == "1":
        number = input("id: ")

        if number in users["students"].keys():
            username = input("username: ")
            password = input("password: ")
            if username in users["students"][number]['username'] and password in str(
                    users["students"][number]["password"]):
                print(d)

                while True:
                    option = input("s: ")

                    if option == "1":

                        print(*users and users["students"][number])
                    elif option == "2":

                        lesson = users["students"][number]['lesson']
                        print(f"Your lessons: {lesson}")
                    elif option == "3":
                        classs = users["students"][number]['class']  # noqa
                        print(f"Your class: {classs}")
                    elif option == "4":
                        homeTask = users["students"][number]['homeTask']
                        print(f"Your home task: {homeTask}")
                    elif option == "5":
                        break
                        print("Dastun To'xtadi!")
                    else:
                        print("xato tanladingiz!")
    if e == "2":
        new_student_id = str(len(users["students"]) + 1)

        new_student = {}

        for key in ["fullname", "username", "password", "grade", "lesson", "class", "homeTask"]:
            value = input(f"Enter {key.replace('','')}: ")
            new_student[key] = value

        new_student["grade"] = int(new_student["grade"])

        users["students"][new_student_id] = new_student

        print(f"Sizning ID raqamingiz -> {new_student_id}")

        with open('users.json', 'w') as file:
            json.dump(users, file, indent=4)

    if e == "3":
        print(users["students"])
