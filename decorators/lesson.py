
# 1
# numbers = [1,2,3,4,1,2,3,4,5,5,6,7,8,9,10]

# b = {}
#
# dict = {}
# for num in numbers:
#     if num in dict:
#         dict[num] += 1
#     else:
#         dict[num] = 1
#
# print(dict)

# 2
# numbers = [1,2,3,4,1,2,3,4,5,5,6,7,8,9,10]
#
# dict = {}
#
# for num in numbers:
#     dict[num] = numbers.count(num)
#
# print(dict)
# 3
# def do_twice(func):
#     def wrapper_do_twice(*args, **kwargs):
#         print("******")
#         func(*args, **kwargs)
#         print("******")
#
#     return wrapper_do_twice
#
#
# @do_twice
# def say_whee(a, b):
#     print(a * b)
#
#
# say_whee(2, 3)

# 4
# def do_twice(func):
#     def wrapper_do_twice(*args):
#         try:
#
#             func(*args)
#         except ZeroDivisionError:
#             print("bunday bo'lib bolmaydi!")
#
#     return wrapper_do_twice
#
# @do_twice
# def boo(s):
#     print(42 / 0)
#
#
# boo(0)