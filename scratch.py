# (L17_2024-01-29-01-12-00)


class Car:

    def __init__(self, model, year, price=0):
        
        assert type(model) is str, "Enter string in model field"
        assert year >= 2010, "Only cars since 2010"
        assert price >= 0, "Prices must be non-negative"

        self.__model = model
        self.year = year
        self.price = price


car1 = Car("BMW X6", 2020)
# print(car1.model)
# print(car1.__model)
# car1.model = 12
print(car1.price)

# აქ აბრუნებს ერორს მე-18 და მე-19 ხაზზე


