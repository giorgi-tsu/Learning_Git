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

class Car:
    wheels = 4
    @staticmethod
    def moving():
        print("I am moving")

class Bmw(Car):
    @staticmethod
    def represent():
        print("I am BMW!")

car1 = Bmw()
print(car1.wheels)


# დავალება 1

class Human:
    hands = 2
    legs = 2
    @staticmethod
    def sings():
        print("Human sings")

class Georgian(Human):
    race = "white"
    @staticmethod
    def dances():
        print("Dances Georgian Dance")

print(Human.hands)
print(Georgian.hands)
print(Georgian.race)
print(Human.sings())
print(Georgian.sings())



