# დავალება 16

# შემსრულებელი: გიორგი ცუცქირიძე

# ბიბლიოთეკების შემოტანა

import re
import csv

## სავარჯიშო 1

# შექმენი წრის კლასი, რომელსაც ექნება მეთოდები საკუთარი 
# პერიმეტრისა და ფართობის გამოსათვლელად.

class Circle:
    
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14*self.radius**2
    
    def perimeter(self):
        return 2*3.14*self.radius

# კლასის შემოწმება

test_circle = Circle(1)

print(test_circle.area())
print(test_circle.perimeter())


## სავარჯიშო 2

# შექმენი კალკულატორის კლასი, საბაზისო არითმეტიკული ოპერაციების
# მეთოდებით.

class Calc:

    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2
    
    def add(self):
        return self.number1 + self.number2

    def subtract(self):
        return self.number1 - self.number2

    def multiply(self):
        return self.number1 * self.number2

    def divide(self):
        return self.number1 / self.number2

# კლასის შემოწმება

test_calc = Calc(10,2)
print(test_calc.add())
print(test_calc.subtract())
print(test_calc.multiply())
print(test_calc.divide())


## სავარჯიშო 3 (არასავალდებულო)




#------------------------------------------------------------------#