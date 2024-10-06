# 1
# def task1(n):
#     nol = 0
#     for a in str(n):
#         nol += int(a)
#     return nol
#
#
# print(task1(123))


# 2

# def small(n):
#     return min(int(a)for a in str(n))
#
# print(small(234565432))

# 3
# def task3(n):
#     k = 1
#     for a in str(n):
#         k *= int(a)
#     return f"Siz kiritgan son: {len(str(n))} / kopaytmasi: {k}"
#
# print(task3(3298))

# 4

# def task4(month):
#     days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
#     if 1 <= month <= 12:
#         return days[month - 1]
#     else:
#         return "Noto'g'ri oy raqami"
#
#
# month = int(input("Oy raqamini kiriting (1-12): "))
# print(f"{month}-oyda {task4(month)} kun bor.")


# 5
# def task5(a, b):
#     for i in range(1, b + 1):
#         print(a)
#
#
# print(task5(2, 3))


# 6

# def kara(n):
#     for i in range(1, 11):
#         s = i * n
#         print(f"{n} * {i} == {s}")
#
#
# n = int(input("Number:"))
# kara(n)