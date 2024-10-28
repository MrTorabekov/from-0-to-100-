# 1  Axborotni o'lchov birliklari va sanoq tizimlari  # noqa

# 1

# def binary(binary):
#     return int(binary, 2)
#
#
# number = "1101"  # Binary 1101 -> Decimal 13
# print("Decimal:", binary(number))


# 2
# def decimal(decimal):
#     return bin(decimal)[2:]
#
# number = 13  # Decimal 13 -> Binary 1101
# print("Binary:", decimal(number))

# 2 Python variables and data types 1-qism (primativ)  # noqa

# 1

# def add(number):
#     return "Juft" if number % 2 == 0 else "Toq"
#
# print(add(4))
# print(add(5))

# 2

# def number(a, b):
#     return a + b, a * b
#
#
# print(number(3, 4))

# 3  Python variables and data types 2-qism (non-primativ)  # noqa

# 1
# def reverse(a):
#     return a[::-1]
#
# print(reverse([1, 2, 3, 4]))

# 2
# def number(numbers):
#     return sum(numbers) / len(numbers)
#
# print(number((1, 2, 3, 4, 5)))

# 4 Python dasturlash tilining operatorlari  # noqa

# 1

# def operator(number):
#     return "10 dan katta" if number > 10 else "10 dan kichik yoki teng"
#
#
# print(operator(15))
# print(operator(8))

# 2

# def numbers(a, b, c):
#     return max(a, b, c)
#
# print(numbers(5,10,3))

# 5 Python String va ularning metodlari  # noqa

# 1

# def remove(text):
#     return text.replace(" ", "")
#
#
# print(remove("Salom dunyo"))

# 2

# def vowels(word):
#     a = "aeiouAEIOU"
#     return sum(1 for char in word if char in a)
#
# print(vowels("Salom"))


# 6 Python if-elif-else operators

# 1

# def person(age):
#     if age < 13:
#         return "Bola"
#     elif 13 <= age <= 19:
#         return "O‘smir"
#     else:
#         return "Katta"
#
#
#
# print(person(10))  # noqa
# print(person(15))
# print(person(25))


# 2

# def number(a, b, c):
#     toq = 0
#     juft = 0 # noqa
#
#     for num in (a, b, c):
#         if num % 2 == 0:
#             juft += 1
#         else:
#             toq += 1
#     return f"Toq: {toq}, Juft: {juft}"   # noqa
#
# print(number(3, 4, 5))



# 7 Python for va while operatorlari  # noqa

# 1
# def numbers():
#     for i in range(1, 101):
#         if i % 2 == 0:
#             print(i, end=" ")
#
#
# numbers()


# 2
# def find(a):
#     return max(a)
#
#
# print(find([1, 5, 3, 9, 2]))


# 8  List va ularning metodlari  # noqa

# 1
# def clear(a):
#     a.clear()
#     return a
#
#
# print(clear([1, 2, 3]))

# 2

# def number(b):
#     a = []
#     for x in b:
#         a.append(x * 2)
#     return a
#
#
# print(number([1, 2, 3]))

# 9 Tuple, set va ularning metodlari  # noqa

# 1
# def sets(set1, set2):
#     return set1.intersection(set2)
#
#
# print(sets({1, 2, 3}, {2, 3, 4}))

# 10   # Lug‘atlar va ularning metodlari  # noqa

# 1

# def keys(my_dict):
#     for key in my_dict.keys():
#         print(key)
#
# my_dict = {'name': 'Diyorbek', 'age': 16, 'city': 'Tashkent'}
# keys(my_dict)

# 2
# def values(my_dict):
#     return sum(my_dict.values())
#
# my_dict = {'a': 10, 'b': 20, 'c': 30}
# total = values(my_dict)
# print(total)


# 11 Amaliy dars (Algorithm)  # noqa

# 1
# number = input("a: ")
# num_list = list(map(float, number.split()))
# average = sum(num_list) / len(num_list)
# print("O'rta arifmetik qiymat:", average)

# 2

def fibonacci(n):
    a = 0
    b = 1
    c = []
    for _ in range(n):
        c.append(a)
        a, b = b, a + b
    return c

n = int(input("Nechta Fibonacci sonini chiqarish kerak?: "))
print(fibonacci(n))
