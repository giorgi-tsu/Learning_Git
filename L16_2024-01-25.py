# ლექცია 16: L16_2024-01-25

# ლექცია ჩატარდა 2024 წლის 25 იანვარს
# თემა: შესავალი ოოპ-ში

#*******************************************************************#

# საჭირო ბიბლიოთეკების შემოტანა 

import os

#*******************************************************************#

# ლექციის კოდი 

# კითხვები წინა მასალებიდან (L14_2024-01-25-)

# აქ შეიყვანე თემის დასახელება (L14_2024-01-25-)

print("\n",
	"-------------------------- part 0 --------------------------",
	"\n")

# მიმდინარე ლექციის თემა (L14_2024-01-25-00-06-25)

print("\n",
	"-------------------------- part 1 --------------------------",
	"\n")

print(os.getcwd())
os.chdir(r".\Lectures")  # სამუშაო დირექტორიის შეცვლა.
print(os.getcwd())



class Human:
    height = 180
    weight = 80
    hair_col  = "brown"
    nationality = "Georgian"
    citizenship = "Georgia"
    @staticmethod
    def works():
        print("Human is working")
    def moves():
        print("Human is moving")
    def sleeps():
        print("Human sleeps")
    def eats():
        print("Human eats!")

print(hex(id(Human)))
print(type(Human))

human_1 = Human()
human_2 = Human()

print(human_1)
print(human_2)



# Topic 2

class Car:
    wheels = 4

    @staticmethod

    def movement():
        print("I am moving...")

car1 = Car()
car2 = Car()

car1.movement()
car1.movement()

print(type(car1))
print(type(car2))
print(type(Car))
print(car1)
print(car2)


car1.name = "BMW"

car1.wheels = 10

print(car1.wheels)
print(car2.wheels)

# Topic 3


class Human:    
    number_of_hands = 2    
    name = "Levani"    

    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    @staticmethod
    def say_hi():
        print("Hello!")

    def represent(self):
        print(f"Hello, my is {self.name}")                 

human1 = Human("Nika", "Tsitskishvili", 28)
human2 = Human("Elene", "Sixarulidze", 25)

human1.represent()
human2.represent()


# Topic 4


class Human:    
    number_of_hands = 2    
    name = "Levani"    

    def __init__(self, name, lastname, age):
        self.name = name
        self.lastname = lastname
        self.age = age

    @staticmethod
    def say_hi():
        print("Hello!")

    def represent(self):
        print(f"Hello, my is {self.name}")

    @classmethod
    def represent2(cls):
        print(f"Hello, my is {cls.name}")

human1 = Human("Nika", "Tsitskishvili", 28)
human2 = Human("Elene", "Sixarulidze", 25)

human1.represent()
human2.represent()
human1.represent2()
human2.represent2()

Human.name = "Zaza"

human1.represent2()
human2.represent2()


# Topic 5

class Human:    
    number_of_hands = 2    
    name = "Levani"    

    def __init__(self):
        self.name = input("Name: ")
        self.lastname = input("Lastname: ")
        self.age = input("Age: ")

    @staticmethod
    def say_hi():
        print("Hello!")

    def represent(self):
        print(f"Hello, my is {self.name}")

    @classmethod
    def represent2(cls):
        print(f"Hello, my is {cls.name}")

# Topic 6
        
# 01:39:00 ვაგრძელებთ წინა ლექციის თამაშს.