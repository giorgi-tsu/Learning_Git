# ლექცია 17: L17_2024-01-29

# ლექცია ჩატარდა 2024 წლის 29 იანვარს
# თემა: შესავალი ოოპ-ში 2

#*******************************************************************#

# საჭირო ბიბლიოთეკების შემოტანა 

import os

#*******************************************************************#

# ლექციის კოდი 

# კითხვები წინა მასალებიდან (L17_2024-01-29-)

# აქ შეიყვანე თემის დასახელება (L17_2024-01-29-)

print("\n",
	"-------------------------- part 0 --------------------------",
	"\n")






# მიმდინარე ლექციის თემა (L17_2024-01-29-00-04-30)

print("\n",
    "-------------------------- part 1 --------------------------",
    "\n")

# print(os.getcwd())
# os.chdir(r".\Lectures")  # სამუშაო დირექტორიის შეცვლა.
print(os.getcwd())

# class Car:
#     wheels = 4
#     @staticmethod
#     def moving():
#         print("I am moving")

# class Bmw(Car):
#     @staticmethod
#     def represent():
#         print("I am BMW!")

# car1 = Bmw()
# print(car1.wheels)


# დავალება 1

# class Human:
#     hands = 2
#     legs = 2
#     @staticmethod
#     def sings():
#         print("Human sings")

# class Georgian(Human):
#     race = "white"
#     @staticmethod
#     def dances():
#         print("Dances Georgian Dance")

# print(Human.hands)
# print(Georgian.hands)
# print(Georgian.race)
# Human.sings()
# (Georgian.sings())    


# მრავადონიანი მემკვიდრეობითობა (L17_2024-01-29-00-27-30)

# class Car:
#     wheels = 4
#     @staticmethod
#     def moving():
#         print("I am moving")

# class Airplane:
#     wings = 2
#     @staticmethod
#     def flying():
#         print("Flying Mode")

# class Bmw(Car, Airplane):
#     @staticmethod
#     def represent():
#         print("I am BMW!")

# car1 = Bmw()
# car1.flying()

# Polymorphism (L17_2024-01-29-00-29-18)

# class Car:
#     wheels = 4
#     @staticmethod
#     def moving():
#         print("I am moving")

# class Airplane:
#     wings = 2
#     @staticmethod
#     def flying():
#         print("Flying Mode")

# class Bmw(Car, Airplane):
#     @staticmethod
#     def represent():
#         print("I am BMW!")
#     @staticmethod
#     def moving():
#         print("BMW is moving")

# car1 = Bmw()
# car1.flying()
# car1.moving()

#######################


# class Car:
#     wheels = 4

#     def __init__(self, year):
#         self.year = year
    
#     @staticmethod
#     def moving():
#         print("Car is moving")

# class BMW(Car):
#     def __init__(self, model, year):
#         self.model = model
#         super().__init__(year)
#     def represent(self):
#         print(f"This is {self.model}")

# car1 = BMW("X5", 2000)
# # car1.represent()
# # car1.moving()
# print(car1.year) 

############

#  2 მშობელი (L17_2024-01-29-00-36-10)

# class Car:
#     wheels = 4

#     def __init__(self, year):
#         self.year = year
    
#     @staticmethod
#     def moving():
#         print("Car is moving")

# class Jet:
#     def __init__(self, wings):
#         self.wings = wings

#     @staticmethod
#     def flying():
#         print("Jet is flying!")

#     @staticmethod
#     def moving():
#         print("Jet is moving")


# class BMW(Car, Jet):
#     def __init__(self, model, year, wings):
#         self.model = model
#         # super().__init__(year)
#         Car.__init__(self, year)
#         Jet.__init__(self, wings)
#     def represent(self):
#         print(f"This is {self.model}")

# car1 = BMW("X5", 2000, 2)
# car1.represent()
# car1.moving()
# print(car1.wings)
# car1.moving()

# print(car1.wings, car1.year)

##############

# polimorphism slides (L17_2024-01-29-00-41-10)

# Encapsulation slides (L17_2024-01-29-00-42-30)

# Encapsulation (L17_2024-01-29-00-44-21)

# class Car:
#     def __init__(self, model, year, price=0):
        
#         assert type(model) is str, "Enter Sting in model field"
#         assert year > 2010, "Only cars since 2010"
#         assert price >= 0, "Non-negative prices are allowed"
#         self.model = model
#         self.year = year
#         self.price = price
    
# car1 = Car("BMW X6", 2020, 1100)
# print(car1.price)
# car1.price = 1000
# print(car1.price)

#####################################
# class Student:

#     def __init__(self, firstname, lastname):
#         self.firstname = firstname
#         self.lastname = lastname
    
#     def get_name(self):
#         return self.firstname
    
#     def set_name(self, text):
#         self.firstname = text
    
# st1 = Student("Giorgi", "Abashidze")

# print(st1.firstname)
# print(st1.get_name())

# st1.set_name("Daviti")
# print(st1.get_name())


# class MyClass():
#     def __init__(self):
#         self.__priv = "I am private"
#         self._prot = " I am protected"
#         self.pub = "I am pulic"
    
# a = MyClass()

# a.pub += " and I can be modified"

#########################


class Car:

    def __init__(self, model, year, price=0):
        
        assert type(model) is str, "Enter string in model field"
        assert year > 2010, "Only cars since 2010"
        assert price >= 0, "Prices must be non-negative"
        
        self.__model = model
        self._year = year
        self.price = price

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    # @model.getter
    # def


# car1 = Car("BMW X6", 2020)

# print(car1.model)

# car1.model = 12

# print(car1.price)
# print(car1._year)

class Car2:
    def __init__(self, price = 0):
        self.__model = "BMW"
        self._year = 2000
        self.price = price

car = Car2(200)

# class ChildCar(Car2):
#     def __init__(self, price):
#         super().__init__(price)
#         print(self.__model)

# mini_cuper = ChildCar(200)

