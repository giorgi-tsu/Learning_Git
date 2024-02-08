# ლექცია 18: L18_2024-02-01

# ლექცია ჩატარდა 2024 წლის 1 თებერვალს
# თემა: მეტაკლასები

#*******************************************************************#

# საჭირო ბიბლიოთეკების შემოტანა 

import os
from typing import Any

#*******************************************************************#

# ლექციის კოდი 

# კითხვები წინა მასალებიდან (L18_2024-02-01-00-02-44)

# დეკორატორის გახსენება (L18_2024-02-01-00-02-44)

print("\n",
	"-------------------------- part 0 --------------------------",
	"\n")


# def dec_func(func):
#     def inner():
#         print("start")
#         func()
#         print("end")
#     return inner


# @dec_func
# def print_numbers():
#     for i in range(3):
#         print(i)

# print_numbers()


# მიმდინარე ლექციის თემა (L18_2024-02-01-00-06-00)

print("\n",
	"-------------------------- part 1 --------------------------",
	"\n")

# print(os.getcwd())
# os.chdir(r".\Lectures")  # სამუშაო დირექტორიის შეცვლა.
# print(os.getcwd())

# def print_numbers():
#     for i in range(3):
#         print(i)

# print(print_numbers)

# class MyDecorator:
#     def __init__(self, func) -> None:
#         self.func = func

#     def __call__(self) -> Any:
#         print("Start")
#         self.func()
#         print("End")

# # obj = MyDecorator(print_numbers)
# # print(obj.func)
# # obj()
# @MyDecorator
# def print_numbers():
#     for i in range(3):
#         print(i)

# print_numbers()

# ეს იგივეა რაც

# class MyDecorator:
#     def __init__(self, func) -> None:
#         self.func = func

#     def __call__(self) -> Any:
#         print("Start")
#         self.func()
#         print("End")

# # obj = MyDecorator(print_numbers)
# # print(obj.func)
# # obj()

# def print_numbers():
#     for i in range(3):
#         print(i)

# print_numbers = MyDecorator(print_numbers)
# print_numbers()

# პუნქტორი (L18_2024-02-01-00-15-30)

class Pyclass:
    def __init__(self, value):
        self.value = value
    
    def find_suitable_func(self):
        if type(self.value) is str:
            return self.__handle_string()
        
        if type(self.value) is int:
            return self.__handle_integer()


    def __handle_string(self):
        print("Handling string", self.value)
    
    def __handle_integer(self):
        print("Handling integer", self.value)

obj = Pyclass(1)
obj.find_suitable_func()

# დესკრიპტორი (L18_2024-02-01-00-22-39)
