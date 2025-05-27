# Reto-04
## The restaurant revisted


```python

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
```

Output:
```
Coke - $5.40
Wine - $20.00
Appel Juice - $6.20
Spring rolls - $10.45
Soup - $5.80
Spaghetti Bolognese - $16.70
Curry - $18.00
Grilled salmon with vegetables - $20.00
Cheesecake - $8.90
Strawberry Donut - $4.67
French Fries - $6.98
Pizza - $11.76
Salad - $4.50

Subtotal: $139.36
Discount: -$13.94
Discount Desserts: -$1.63
Discount Kids Menu: -$3.53
Total Discount: -$19.09
Total Due: $120.27
Would you like to pay in cash or with card?
The total price is 54.7
The total price is 13.57
The total price is 31.599999999999998
Paying 120.26760000000002 with card 8596
Payment made in cash. Change: 4879.7324
```
