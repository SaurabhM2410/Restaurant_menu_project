# Our Restaurant's Menu Of Dishes With Prices
Menu = {
    "Pizza" : 150,
    "Burger" : 50, 
    "Noodles" : 40,
    "Cold Coffe" : 35,
    "Dimsum" : 80
}
# Greeting for custumers
print("Welcome to Python Restaurant")
print('Pizza : 150\nBurger : 50\nNoodles : 40\nCold Coffe : 35\nDimsum : 80')

# bill amount
order_total = 0

item_1 = input("Enter the name of item you want to order = ")
if item_1 in Menu:
    order_total += Menu[item_1] # EX- Initial_order = 0 + item_1 price
    print(f"Your item {item_1} has been added to your order")
else:
    print("Ordered item {item_1} is not available yet!")
    
another_order = input("Do you want to add another item? (Yes/No) ")

if another_order == "Yes":
    item_2 = input("Enter the name of 2nd item you want to order = ")  
    if item_2 in Menu:  
       order_total += Menu[item_2]
       print(f"Your item {item_2} has been added to your order")
    
    else:
       print(f"Ordered item {item_2} is not available!")
       
print(f"your total amount of items is to pay is rs.{order_total}/-")