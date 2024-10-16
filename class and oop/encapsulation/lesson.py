class Card:
    def __init__(self,fullname,gender,year,address,idcard):
        self.fullname = fullname
        self.gender = gender
        self.year = year
        self.address = address
        self.__idcard = idcard

    def get_id(self):       # yashiringan ma'lumotni ko'rish    # noqa
        return self.__idcard

    def __get_idcard(self):
        return self.__idcard

person = Card("Diyorbek","Male",2000,"Tashkent","AB2323")

print(person.get_id())
# print(person.get_idcard())    # bu ishlamaydi chunki class ni ichidagi method nomi ham __ bilan yozilgan  # noqa
