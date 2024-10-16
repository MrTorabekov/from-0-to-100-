# class Myclass:
#     class_var = 0
#     def __init__(self,value):
#         self.value = value
#
#     @classmethod
#     def increment_cls(cls):
#         cls.class_var += 1
#         return cls.class_var
#
# print(Myclass.increment_cls())
# print(Myclass.increment_cls())


class Person:
    @staticmethod
    def great(name):
        return f"bye {name}"
print(Person.great("Diyorbek"))