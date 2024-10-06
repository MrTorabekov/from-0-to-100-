# menu = """1.Accept Student
# 2.All    Student
# 3.Search Student
# 4.Delete Student
# 5.Update Student
# 6.Exit
# """
# users = []
# while True:
#     x = input(menu)
#     if int(x) == 1:
#         user = input("student name: ")
#         users.append(user)
#         print(f"add student: {user}")
#
#     elif int(x) == 2:
#         print(users)
#
#     elif int(x) == 3:
#         a = input("Sizga qaysi student kerak:")
#         if a in users:
#             print(f"Ha {a} bor")
#         else:
#             print("Bunday oquvchi yoq yoki notori ma'lumot kiritdingiz!")
#
#     elif int(x) == 4:
#         delete = input("Siz qaysi studentni o'chirmoqchisiz:")
#         if delete in users:
#             users.remove(delete)
#             print("o'chirildi")
#         else:
#             print("bunday student yoq")
#
#     elif int(x) == 5:
#         update = input("Kimni update qilmoqchisiz")
#         if update in users:
#             update2 = input("yangi ism kiriting:")
#             users.append(update2)
#             users.remove(update)
#             print("Foydalanuvchi o'zgartirildi!")
#     elif int(x) == 6:
#         print("Dastur toctatildi!")
#         break


# old = [ 1, 2, 3, 4, 5, 6, 7,
#     3, 4, 5, 6, 7, 8, 9,
#     12, 34, 45, 56, 57,
#     31, 21, 43, 13, 45
# ]
# new = []
# for i in old:
#     if i % 5 == 0:
#         new.append(i)
# print(new)

# old = [ [1, 2, 3, 4, 5, 6, 7],[3, 4, 5, 6, 7, 8, 9],[12, 34, 45, 56, 57],[31, 21, 43, 13, 45]]
# new = []
# for i in old:
#     for n in i:
#         if n % 5 == 0:
#             new.append(n)
# print(new)

