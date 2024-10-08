#  Python Function -> Pythondagi funksiya     # noqa

# def add_one(number):
#     return number + 1
#
#
# print(add_one(2))


# First-Class Objects -> Birinchi darajali ob'ektlar  # noqa

# def say_hello(name):
#     return f"Hello {name}"
#
# def be_awesome(name):
#     return f"Yo {name}, together we're the awesomest!"
#
# def greet_bob(greeter_func):
#     return greeter_func("Bob")
#
# print(say_hello("Torabekov_08"))
# # ==============================
# print(be_awesome("Diyorbek"))
# # ==============================
# print(greet_bob(say_hello))
# # ==============================
# print(greet_bob(be_awesome))
# # ==============================


# Inner Functions -> Ichki funksiyalar    # noqa

# 1

# def parent():
#     print("Printing from parent()")
#
#     def first_child():
#         print("Printing from first_child()")
#
#     def second_child():
#         print("Printing from second_child()")
#
#     first_child()
#     second_child()
#
# parent()

# 2

# def parent(num):
#     def first_child():
#         return "Hi, I'm Elias"
#
#     def second_child():
#         return "Call me Ester"
#
#     if num == 1:
#         return first_child
#     else:
#         return second_child
#
# first = parent(1)
# second = parent(2)
#
# print(first())
# print(second())


# Simple Decorators in Python -> Pythonda oddiy dekorativlar   # noqa

# 1

# def decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper
#
# def say_whee():
#     print("Whee!")
#
# say_whee = decorator(say_whee)
#
# say_whee()

# 2

# from datetime import datetime


# def not_during_the_night(func):
#     def wrapper():
#         if 7 <= datetime.now().hour < 22:
#             func()
#         else:
#             pass  # Hush, the neighbors are asleep
#     return wrapper
#
# def say_whee():
#     print("Whee!")
#
# say_whee = not_during_the_night(say_whee)
# say_whee()

# Adding Syntactic Sugar -> Sintactic shakar qo'shish   #noqa

# def decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#
#     return wrapper
#
#
# @decorator
# def say_whee():
#     print("Whee!")
#
# say_whee = decorator(say_whee)
# say_whee()


# Reusing Decorators -> Dekoratorlarni qayta ishlatish  # noqa

# 1

# def do_twice(func):
#     def wrapper_do_twice():
#         func()
#         func()
#     return wrapper_do_twice
#
# @do_twice
# def say_whee():
#     print("Whee!")
#
# say_whee()

# Decorating Functions With Arguments -> Funksiyalarni Argumentlar bilan bezash     # noqa

# 1

# def do_twice(func):
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#         func(*args, **kwargs)
#     return wrapper_do_twice
#
#
# @do_twice
# def greet(name):
#     print(f"Hello {name}")
#
# greet(name="World")

# 2

# def do_twice(func):
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#         func(*args, **kwargs)
#
#     return wrapper_do_twice
#
# @do_twice
# def say_whee():
#     print("Whee!")
#
#
# say_whee()
#
#
#
# @do_twice
# def greet(name):
#     print(f"Hello {name}")
#
#
# greet("World")


# Returning Values From Decorated Functions

# 1

# def do_twice(func):
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#
#
#     return wrapper_do_twice
# @do_twice
# def return_greeting(name):
#     print("Creating greeting")
#     print( f"Hi {name}")
#
#
# hi_adam = return_greeting("Adam")


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


def do_twice(func):
    def wrapper_do_twice(*args):
        try:

            func(*args)
        except ZeroDivisionError:
            print("bunday bo'lib bolmaydi!")

    return wrapper_do_twice

@do_twice
def boo(s):
    print(42 / 0)


boo(0)
