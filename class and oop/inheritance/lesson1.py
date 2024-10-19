'''
Car: name,year,engine :  Super class
moving() True bolsa moshin harakatlanayabdi 

BMW: color, speed,price,model : Sub class
display() BMW info 
'''  # noqa


# class Car:
#     def __init__(self, name, year, engine: bool):
#         self.name = name
#         self.year = year
#         self.engine = engine
#
#     def moving(self):
#         if self.engine:
#             print("Auto started")
#         else:
#             print("Auto stopped")
#
#
# class BMW(Car):
#     def __init__(self, name, year, engine, color, speed, price, model):
#         super().__init__(name, year, engine)
#         self.color = color
#         self.speed = speed
#         self.price = price
#         self.model = model
#
#     def display(self):
#         return f"BMW Feature\ncolor: {self.color}\nmodel: {self.model}\nyear: {self.year}\nspeed: {self.speed}"
#
#
# bmw = BMW("BMW", 2024, True, "Blue", 200, 200_000, "M7")
# bmw1 = BMW("BMW", 2024, False, "Blue", 200, 200_000, "M7")
#
# # bmw.moving()
# # bmw1.moving()
# print(bmw1.display())


# ===============================================================================================

'''
Car: name,year,engine,petrol:int:  Super class
moving() True bolsa moshin harakatlanayabdi 

BMW: color, speed,price,model: Sub class
display() BMW info
chack() 
'''  # noqa


class Car:
    def __init__(self, name, year, engine: bool, petrol: int):
        self.name = name
        self.year = year
        self.engine = engine
        self.petrol = petrol


    def moving(self):
        if self.engine:
            print("Auto started")
        else:
            print("Auto stopped")

    def chack(self):        # noqa
        if self.petrol != 0 and self.engine == True:
            print("running")
        else:
            print("no petrol")


class BMW(Car):
    def __init__(self, name, year, engine, petrol, color, speed, price, model):
        super().__init__(name, year, engine, petrol)
        self.color = color
        self.speed = speed
        self.price = price
        self.model = model

    def display(self):
        return f"BMW Feature\ncolor: {self.color}\nmodel: {self.model}\nyear: {self.year}\nspeed: {self.speed}"


bmw = BMW("BMW", 2024, True, 12, "Bule", 200, 200_000, "M7")
bmw1 = BMW("BMW", 2024, False, 24, "Bule", 200, 200_000, "M7")

# bmw.moving()
# bmw1.moving()
# print(bmw1.display())
bmw.chack()
bmw1.chack()
