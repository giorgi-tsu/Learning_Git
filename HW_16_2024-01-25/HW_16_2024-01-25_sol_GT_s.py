# დავალება 16

# შემსრულებელი: გიორგი ცუცქირიძე

# ბიბლიოთეკების შემოტანა

import math


## სავარჯიშო 1

# შექმენი წრის კლასი, რომელსაც ექნება მეთოდები საკუთარი 
# პერიმეტრისა და ფართობის გამოსათვლელად.

class Circle:
    
    def __init__(self, radius):
        self.radius = radius

    def calc_area(self):
        area = math.pi * (self.radius ** 2)
        return area

    def calc_perimeter(self):
        perimeter = 2 * math.pi * self.radius
        return perimeter

# კლასის შემოწმება

radius = 1
circle_instance = Circle(radius)

print(f"Area of a circle with radius of {radius}: "
      f"{circle_instance.calc_area()}")
       
print(f"Perimeter of a circle with radius of {radius}: "
      f"{circle_instance.calc_perimeter()}")


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

calc_instance = Calc(10,2)
print(calc_instance.add())
print(calc_instance.subtract())
print(calc_instance.multiply())
print(calc_instance.divide())


## სავარჯიშო 3 (არასავალდებულო)

# შექმენი შოფინგის კალათის კლასი, რომელსაც ექნება მეთოდები
# სასურველი ნივთის დასამატებლად და ამოსაშლელად,
# ასევე კალათაში არსებული პროდუქტების სიისა და
# ჯამური ღირებულების გამოსატანად. 


class ShoppingBasket:

    def __init__(self):

        self.item_prices = {}
        self.item_quantities = {}

    def add_item(self, item, quantity, price):
        self.item_quantities[item] = quantity
        self.item_prices[item] = price

    def delete_item(self, item):
        del self.item_quantities[item]
        del self.item_prices[item]

    def get_shopping_list(self):
        return list(self.item_quantities.keys())

    def total_basket_value(self):
        total_value = 0
        for p, q in zip(self.item_prices.values(),
                        self.item_quantities.values()):
          total_value += p * q
        return total_value

basket_instance = ShoppingBasket()

# Adding items to the shopping basket

basket_instance.add_item("Milka", 2, 2)
basket_instance.add_item("Sante", 3, 1)
basket_instance.add_item("Koda", 3, 5)

print(f"Shopping List: {basket_instance.get_shopping_list()}")
print(f"Item Prices: {basket_instance.item_prices}")
print(f"Item Quantities: {basket_instance.item_quantities}")

basket_instance.delete_item("Sante")  # Deleting "Sante" from 
# the shopping basket

print(f"Shopping List: {basket_instance.get_shopping_list()}")
print(f"Item Prices: {basket_instance.item_prices}")
print(f"Item Quantities: {basket_instance.item_quantities}")



print(f"Total Value of Shopping List: "
      f"{basket_instance.total_basket_value()}")


#------------------------------------------------------------------#