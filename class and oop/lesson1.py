# Python class and objects
# class ClassName:
#     # < statement - 1 >
#     # .
#     # .
#     # .
#     # < statement - N >
#     ...


# class MyClass:
#     # instance attribute
#     name = "Jack"
#     age = 17
#
#
# # object
# childClass = MyClass()
#
# print(childClass.name)
# print(childClass.age)


# class MyClass:
#     # instance attribute
#     name = "Jack"
#     age = 17
#
#     def display(self):
#         '''class data get '''
#         return f"name: {self.name}\nage: {self.age}"
#
#
# # object
# childClass = MyClass()
#
# # print(childClass.display())
# # print(childClass.display.__doc__) # class function in docs get


# class MyClass:
#
#     def __init__(self, name, age, address):
#         self.name = "Musharraf"
#         self.age = 24,
#         self.address = "Tashkent"
#
#
# obj = MyClass("Bob", 18, "London")
# print(obj.name)


# class MyClass:
#
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#
#     def info(self):
#         return f"Name: {self.name}\nage: {self.age}\naddress: {self.address}"


# obj = MyClass("Bob", 18, "London")
#
# obj1 = MyClass("Anna", 18, "Russia")
#
# obj2 = MyClass("Safia", 17, "Germany")
# print(obj.info())
# print(obj1.info())
# print(obj2.info())


# class Myclass:
#     def __init__(self, name, age, address):
#         self.name = name
#         self.age = age
#         self.address = address
#
#     def func(self):
#         return self.name, self.age, self.address
#
#
# obj = Myclass(name="Diyorbek",age=12,address="tashkent")
# ob1 = Myclass(name="Torabekov",age=12,address="Uzbekistan")
#
# print(obj.func())
# print(ob1.func())
#


# class All:
#     def __init__(self,number,numbers):
#         self.number = number
#         self.numbers = numbers
#
#
#     def num(self):
#         return (f"Qo'shish: {self.number + self.numbers} |"
#                 f"ayirish: {self.number - self.numbers } |"
#                 f"kopaytirish: {self.number * self.numbers} |"
#                 f"Bo'lish: {self.number // self.numbers} |"
#                 f"foiz: {self.number % self.numbers} |")
#
#
# obj = All(10,19)
#
# print(obj.num())
