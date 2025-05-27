class Menultem:
    def __init__(self, name: str, price: float):
        self._name = name
        self._price = price

    def total_price(self, *args: "Menultem") -> float:
        sum: float = self._price

        for i in args:
            sum += i._price
        return f"The total price is {sum}"
    
    def get_price(self):
        return self._price
    
    def get_name(self):
        return self._name
    
    def set_price(self, new_price):
        self._price = new_price

    def set_name(self, new_name):
        self._name = new_name

    def __str__(self):
        return f"{self._name} - ${self._price:.2f}"


class Beverages(Menultem):
    def __init__(self, name, price, alcohol: bool):
        super().__init__(name, price)
        self._alcohol = alcohol
    
    def get_alcohol(self):
        return self._alcohol

    def set_alcohol(self, new_alcohol):
        self._alcohol = new_alcohol
        

class Starters(Menultem):
    def __init__(self, name, price, portion: str):
        super().__init__(name, price)
        self._portion = portion
    
    def get_portion(self):
        return self._portion

    def set_portion(self, new_portion):
        self._portion = new_portion


class MainCourse(Menultem):
    def __init__(self, 
                name, 
                price, 
                protein: str, 
                spicy: bool, 
                vegetarian: bool):
        super().__init__(name, price)
        self._protein = protein
        self._spicy = spicy
        self._vegetarian = vegetarian

    def get_protein(self):
        return self._protein
    
    def get_spicy(self):
        return self._spicy
    
    def get_vegetarian(self):
        return self._vegetarian
    
    def set_protein(self, new_protein):
        self._protein = new_protein

    def set_spicy(self, new_spicy):
        self._spicy = new_spicy

    def set_vegetarian(self, new_vegetarian):
        self._vegetarian = new_vegetarian

class Desserts(Menultem):
    def __init__(self, 
                name, 
                price, 
                level_sugar: str, 
                gluten_free: bool):
        super().__init__(name, price)
        self._level_sugar = level_sugar
        self._gluten_free = gluten_free
    
    def get_level_sugar(self):
        return self._level_sugar
    
    def get_gluten_free(self):
        return self._gluten_free
    
    def set_level_sugar(self, new_level_sugar):
        self._level_sugar = new_level_sugar

    def set_gluten_free(self, new_gluten_free):
        self._gluten_free = new_gluten_free


class Extras(Menultem):
    def __init__(self, name, price, with_sausage: bool):
        super().__init__(name, price)
        self._with_sausage = with_sausage

    def get_with_sausage(self):
        return self._with_sausage
    
    def set_with_sausage(self, new_with_sausage):
        self._with_sausage = new_with_sausage
        

class KidsMenu(Menultem):
    def __init__(self, name, price, haealthy: bool):
        super().__init__(name, price)
        self._healthy = haealthy

    def get_haealthy(self):
        return self._haealthy
    
    def set_level_sugar(self, new_haealthy):
        self._haealthy= new_haealthy


class Order:
    def __init__(self, *args: Menultem):
        self.items = [*args]
    
    def add_items(self, item: "Menultem"):
        self.items.append(item)
    
    def bill_amount(self) -> float:
        sum = 0
        for i in self.items:
            sum += i._price
        return sum
    
    def discount(self, percent: float) -> float:
        total: float = self.bill_amount()
        discounted: float = total * percent / 100
        return discounted
    
    def discount_desserts(self) -> float:
        counter: int = 0
        desserts: float = 0
        for i in self.items:
            if isinstance(i, Beverages):
                counter += 1
            if isinstance(i, Desserts):
                desserts += i._price

        discounted: float = desserts * counter * 4 / 100
        return discounted

    def discount_kids_menu(self) -> float:
        counter: int = 0
        kids_menu: float = 0
        for i in self.items:
            if isinstance(i, MainCourse):
                counter += 1
            if isinstance(i, KidsMenu):
                kids_menu += i._price

        discounted: float = kids_menu * counter * 10 / 100
        return discounted
    
    def total_bill_amount(self, percent) -> float:
        subtotal = self.bill_amount()
        discount = self.discount(percent)
        discount_desserts = self.discount_desserts()
        discount_kids_menu = self.discount_kids_menu()
        total_discount = discount + discount_desserts + discount_kids_menu
        return  subtotal - total_discount

    def print_bill(self, percent: float):
        for item in self.items:
            print(f"{item}")

        discount = self.discount(percent)
        discount_desserts = self.discount_desserts()
        discount_kids_menu = self.discount_kids_menu()
        total_discount = discount + discount_desserts + discount_kids_menu

        print(f"\nSubtotal: ${self.bill_amount():.2f}")
        print(f"Discount: -${discount:.2f}")
        print(f"Discount Desserts: -${discount_desserts:.2f}")
        print(f"Discount Kids Menu: -${discount_kids_menu:.2f}")
        print(f"Total Discount: -${total_discount:.2f}")
        print(f"Total Due: ${self.total_bill_amount(percent):.2f}")
        print("Would you like to pay in cash or with card?")

class Payment:
    def __init__(self):
        pass

    def pay(self, amount: float):
        raise NotImplementedError("You have to choose a payment method.")

class Card(Payment):
    def __init__(self, number: str, cvv: int):
        super().__init__()
        self.number = number
        self.cvv = cvv

    def pay(self, amount: float):
        print(f"Paying {amount} with card {self.number[-4:]}")

class Cash(Payment):
    def __init__(self, amount_given: float):
        super().__init__()
        self.amount_given = amount_given

    def pay(self, amount: float):
        if self.amount_given >= amount:
            print(f"Payment made in cash. Change: {self.amount_given - amount}")
        else:
            print(f"Insufficient funds. Missing {amount - self.amount_given} for complete the payment.")


menu = Order(
            Beverages("Coke", 5.4, False), 
             Beverages("Wine", 20, True), 
             Beverages("Appel Juice", 6.2, False), 
             Starters("Spring rolls", 10.45, "Small"), 
             Starters("Soup", 5.8, "Medium"), 
             MainCourse("Spaghetti Bolognese", 16.7, "Meat", False, False),
             MainCourse("Curry", 18, "Tofu", True, True),
             MainCourse("Grilled salmon with vegetables", 20, "Salmon", False, False),
             Desserts("Cheesecake", 8.9,"Medium", False),
             Desserts("Strawberry Donut", 4.67, "High", True),
             Extras("French Fries", 6.98, True),
             KidsMenu("Pizza", 11.76, False))
menu.add_items(Extras("Salad", 4.5, False))
menu.print_bill(10)
main_course1 = MainCourse("Spaghetti Bolognese", 16.7, "Meat", False, False)
main_course2 = MainCourse("Curry", 18, "Tofu", True, True)
main_course3 = MainCourse("Grilled salmon with vegetables", 20, "Salmon", False, False)
dessert1 = Desserts("Strawberry Donut", 4.67, "High", True)
dessert2 = Desserts("Cheesecake", 8.9,"Medium", False)
beverage1 = Beverages("Coke", 5.4, False)
beverage2 = Beverages("Wine", 20, True)
beverage3 = Beverages("Appel Juice", 6.2, False)

print(main_course1.total_price(main_course2, main_course3))
print(dessert1.total_price(dessert2))
print(beverage1.total_price(beverage2, beverage3))

card= Card("15263748596", 707)
card.pay(menu.total_bill_amount(10))
cash = Cash(5000)
cash.pay(menu.total_bill_amount(10))