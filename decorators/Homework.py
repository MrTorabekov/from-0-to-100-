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
        "3":{
            "fullname": "Diyorbek",
            "username": "Torabekov_08",
            "password": 2222,
            "grade": None,
            "lesson": "english",
            "class": "10b23",
            "homeTask": "Def func"
        }

    }
}

teach_pr = {
    "fullname": "Diyorbek",
    "username": "Diyor",
    "password": 1,
    "class":"10b23"
}

my = """
1. my profile
2. my lesson
3. my class
4. homeTask
5. Break
"""

find = """
siz kimsiz?
1. Teacher
2. Student
->:"""

teach = """
1. profile
2. classes
3. add grade
3. remove students
Sizga qaysi biri kerak: """


# data types for while

while 1:
    check = input(find)
    if check == '1':
        print("Siz Login qilishingiz kerak!")
        username = input("username: ")
        password = input("password: ")

        if username in teach_pr['username'] and password in str(teach_pr["password"]):
            determine = input(teach)
            if determine == '1':
                print(teach_pr)
            elif determine == '2':
                print(teach_pr['class'])
            elif determine == '3':
                student_id = input("O'quvchi ID sini kiriting: ")

                if student_id in users["students"]:
                    if teacher_mode:
                        student = users["students"][student_id]

                        if student["grade"] is None:
                            print(f"{student['fullname']} uchun hali baho qo'yilmagan.")
                            new_grade = int(input(f"{student['fullname']} uchun yangi bahoni kiriting: "))
                        else:
                            print(f"{student['fullname']}ning hozirgi bahosi: {student['grade']}")
                            change = input("Bahoni o'zgartirmoqchimisiz? (ha/yo'q): ").lower()

                            if change == "ha":
                                new_grade = int(input(f"{student['fullname']} uchun yangi bahoni kiriting: "))
                            else:
                                new_grade = student["grade"]

                        student["grade"] = new_grade
                        print(f"O'quvchining yangi bahosi: {student['grade']}")








    e = str(input(f"{s}:"))
    if e == "1":
        number = input("id: ")

        if number in users["students"].keys():

            if username in users["students"][number]['username'] and password in str(
                    users["students"][number]["password"]):
                print(my)

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
            value = input(f"Enter {key.replace('', '')}: ")
            new_student[key] = value

        new_student["grade"] = int(new_student["grade"])

        users["students"][new_student_id] = new_student

        print(f"Sizning ID raqamingiz -> {new_student_id}")

        with open('users.json', 'w') as file:
            json.dump(users, file, indent=4)

    if e == "3":
        print(users["students"])
