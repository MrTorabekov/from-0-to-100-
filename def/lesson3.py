# def movZero(nums: list):
#     count = 0
#     for i in range(len(nums)):
#         if nums[i] != 0:
#             nums[count], nums[i] = nums[i], nums[count]
#             count += 1
#     return nums

# print(movZero([1,0,4,0]))


# def movZero(nums: list):
#     for i in range(len(nums)):
#         if nums[i] == 0:
#             nums.append(nums.pop(i))
#             i -= 1
#     return nums

# print(movZero([1,0,4,0]))

# ------------------------------------------------------------------------

# Task 1

# def docstring(a, b):
#     """a va b ni qo'shib bermoqda"""
#     return a + b

# print(docstring(1, 2))

# Task 2

# def docstringTrue(a: int, b: int):
#     """
#     integer kiriting
#     """
#     return a + b

# print(docstringTrue(1, 2))

# Task 3

# def args(*args):
#     """
#     *args: bu funksiya argumentlar qatorini qabul edadi
#     """
#     natija = 0
#     for i in args:
#         natija += i
#     return natija

# print(args(1, 2, 3, 4, 5))

# Task 4

def kwargs(**kwargs):
    """
    **kwargs: bu funksiya key-value pairlar qatorini qabul edadi
    """
    for v in kwargs.values():
        print(v, end=' ')

kwargs(a='Diyorbek', b=16, c='Male')
