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



# 2

class All:
    def __init__(self,number,numbers):
        self.number = number
        self.numbers = numbers


    def num(self):
        return (f"Qo'shish: {self.number + self.numbers} |"
                f"ayirish: {self.number - self.numbers } |"
                f"kopaytirish: {self.number * self.numbers} |"
                f"Bo'lish: {self.number // self.numbers} |"
                f"foiz: {self.number % self.numbers} |")


obj = All(10,19)

print(obj.num())

