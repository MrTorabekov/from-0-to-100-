''' HomeWork 
Car: name,year,engine,petrol:int:  Super class
moving() True bolsa moshin harakatlanayabdi 

BMW: color, speed,price,model,tm: Sub class
display() BMW info
chack() 
show() petrol necha km ga yetadi
tm = 10 har 100 mk 10 liter ishlatadi
'''  # noqa


class Cars:
    def __init__(self, name, year, engine: bool, petrol: int):
        self.name = name
        self.year = year
        self.engine = engine
        self.petrol = petrol

    def moving(self):
        if self.engine:
            print("Started")
        else:
            print("Stoped")

    def check(self):
        if self.petrol != 0 and self.engine == True:
            print("run")
        else:
            print("no petrol or engine == false")

    def show(self):
        if self.petrol > 0:
            a = self.petrol * 10
            print(f"Sizning benziningiz -> {a} km ga yetadi")
        else:
            print("Sizning benziningiz yo'q")


class Car(Cars):
    def __init__(self, name, year, engine, petrol, color, speed, price, model):
        super().__init__(name, year, engine, petrol)
        self.color = color
        self.speed = speed
        self.price = price
        self.model = model

    def display(self):
        return f"color -> {self.color}\nspeed -> {self.speed}\nprice -> {self.price}\nmodel -> {self.model}"


mers = Car("Gelik", 2022, True, 10, "Black", 350, 40000.00, "MERS")
copy = Car("Gelik", 2022, False, 10, "Black", 350, 40000.00, "MERS")
print(mers.display())
# mers.show()
# mers.check()
# mers.moving()
