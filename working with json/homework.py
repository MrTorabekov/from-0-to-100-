import json

# 2

b = [
    {"name": "lola", "age": 17, "grade": "A"},
    {"name": "Olim", "age": 24, "grade": "B"},
    {"name": "Ali", "age": 33, "grade": "C"},
]

# json_obj = json.dumps(b, indent=4)
#
# with open('students.json','w') as files:
#     files.write(json_obj)


# 3

with open("student.json",'r') as file:
    data = json.load(file)

    for student in data:
        if student['name'] == 'Ali':
            student['age'] = 28


    with open('student.json', 'w') as file:
        json.dump(data, file, indent=4)

    print("Alining yoshi muvaffaqiyatli o'zgartirildi.\n")
    print("4-Task")
# 4

    for i in data:
        if i['age'] >= 21:
            print(i['name'])

