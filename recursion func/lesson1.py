# def count_down(start):
#     print(start)
#     x = start - 1
#     if x > 0:
#         count_down(start -1)
#
# count_down(7)

# def func(n):
#     data = 1
#
#     for i in range(n + 1 ):
#         data += i
#     return data
#
#
# print(func(10))

# def func(n):
#     data = 1
#
#     for i in range(1,n + 1):
#         data *= i
#     return data
#
#
# print(func(3))

# def fact(n):
#     if n == 1:
#         return n
#
#     elif n > 1:
#         return fact(n - 1) * n
#     else:
#         print(f"noldan katta son kiriting!")
#
#
# print(fact(3))


# def func(n):
#
#     if n == 0:
#         return 0
#     elif n == 1 or n == 2:
#         return 1
#     else:
#         return func(n - 1) + func(n - 2)
#
# print(func(15))