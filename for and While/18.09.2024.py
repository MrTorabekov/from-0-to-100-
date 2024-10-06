# menu = """
# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Division
# 5. History
# 6. Exit
# which one:
# """
# history = []
# while 1:
#     x = input(menu)
#     if int(x) == 1:
#         add = int(input("Enter number:"))
#         add2 = int(input("Enter second number:"))
#         a = add + add2
#         history.append(f" add -> {a}")
#         print(a)
#
#     elif int(x) == 2:
#         Sub = int(input("Enter number:"))
#         Sub2 = int(input("Enter second number:"))
#         b = Sub - Sub2
#         history.append(f"Subtract -> {b}")
#         print(b)
#
#     elif int(x) == 3:
#         Mul = int(input("Enter number:"))
#         Mul2 = int(input("Enter second number:"))
#         c = Mul * Mul2
#         history.append(f"Multiply -> {c}")
#         print(c)
#
#     elif int(x) == 4:
#         Div = int(input("Enter number:"))
#         Div2 = int(input("Enter second number:"))
#         d = Div // Div2
#         history.append(f"Division -> {d}")
#         print(d)
#
#     elif int(x) == 5:
#         print(history)
#
#     elif int(x) == 6:
#         print("Program stop!")
#         break
#
#     else:
#         print("not found")

# =======================================================

# menu = """
# 1. Add task
# 2. Remove task
# 3. Tasks list
# 4. Exit
# Which one:"""
#
# Task = []
#
# while 1:
#     x = input(menu)
#
#     if int(x) == 1:
#         add = input("write task:")
#         Task.append(add)
#         print("your task is success add!")
#
#     elif int(x) == 2:
#         remove = input("which task do you want to remove:")
#         if remove in Task:
#             Task.remove(remove)
#             print("Task is success remove!")
#         else:
#             print("this is task not found.")
#
#     elif int(x) == 3:
#         print(Task)
#
#     elif int(x) == 4:
#         print("Program stop!")
#         break
#
#     else:
#         print("not found")
