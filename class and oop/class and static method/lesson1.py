# 1

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

# 2
# class Person:
#     @staticmethod
#     def great(name):
#         return f"bye {name}"
# print(Person.great("Diyorbek"))

# 3

# class Math:
#     @staticmethod
#     def number(a,b):
#         return a**b
# print(Math.number(2,3))

# 4

class BankAccount:
    bank_users = 0

    def __init__(self, fullname, balance=0):
        self.fullname = fullname
        self.balance = balance
        BankAccount.bank_users += 1

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print(f"sizda yetarli pul yo'q. siz {self.balance}")  # noqa

    @classmethod
    def get_users_accounts(cls):
        return f"Bank users: {cls.bank_users}"

    @staticmethod
    def investors(balance, rate):
        return balance * rate / 100


# Hisoblar ochamiz # noqa
    def __str__(self):
        return f"name : {self.fullname} balance : {self.balance}"

users1 = BankAccount("Firdavs", 500)
users2 = BankAccount("Jamol", 1000)
print(users1)
print(users2)

# Mablag' qo'shish va yechib olish # noqa
users1.deposit(400)
users2.withdraw(500)

# bank all users get
print(BankAccount.get_users_accounts())

# Investor
investor = BankAccount.investors(1000, 5)

print(f"Foyiz: {investor}")

