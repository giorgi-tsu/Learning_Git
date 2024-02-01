# დავალება 16

# შემსრულებელი: გიორგი ცუცქირიძე

# ეს დავალება მოგვცეს მეთექვსმეტე ლექციაზე, რომელიც ჩატარდა 
# 2024-01-25-ში და დავალების ჩაბარების ბოლო ვადაა 2024-02-01.

#******************************************************************#

print("\n",
      "-------------------- სავარჯიშო 1 --------------------", "\n")

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


print("\n",
      "-------------------- სავარჯიშო 2 --------------------", "\n")

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


print("\n",
      "-------------------- სავარჯიშო 3 --------------------", "\n")

## სავარჯიშო 3

# შექმენი შოფინგის კალათის კლასი, რომელსაც ექნება მეთოდები
# სასურველი ნივთის დასამატებლად და ამოსაშლელად,
# ასევე კალათაში არსებული პროდუქტების სიისა და
# ჯამური ღირებულების გამოსატანად. 

class Basket:

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
    
    # def total_basket_value(self):
        
    #     return 

carrefour_basket = Basket()
carrefour_basket.add_item("Milka", 2, 2)
carrefour_basket.add_item("Sante", 3, 1)
carrefour_basket.add_item("Koda", 3, 5)
# carrefour_basket.delete_item("Sante")
print(carrefour_basket.get_shopping_list())
print(carrefour_basket.item_prices)
print(carrefour_basket.item_quantities)


print("\n",
      "-------------------- სავარჯიშო 3 --------------------", "\n")

## სავარჯიშო 4




#------------------------------------------------------------------#