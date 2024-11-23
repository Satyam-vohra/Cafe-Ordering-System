                                  # CAFE ITEMS LIST
menu = {
    "Pizza": 199,
    "Pasta": 79,
    "Burger": 69,
    "Coffee": 69,
    "Coldrink": 49,
    "Sandwich": 49,
    "Pita Bread": 29,
    "Garlic Bread": 79,
    "Brownie": 49
}

# Greet
print('\033[94m''\033[01m'"WELCOME TO VOHRA's CAFE".center(120))
print('\033[35m'"Menu:")
for item, price in menu.items():
    print(f"{item}: {price} Rs")

order_total = 0  # order total

while True:
    item = input('\033[93m'"\nEnter the name of the item you want to order (or type 'cancel' to cancel your order): ")
    
    if item == "cancel":
        print('\033[31m'"Your order has been canceled. Starting a new order...")
        order_total = 0  # Reset order total
        continue  # Restart the loop for a new order
    
    if item in menu:
        order_total += menu[item]
        print(f"Your item '{item}' has been added to your order.")
    else:
        print('\033[90m'"The item you requested is not available. Please order something else.")
    
    another_order = input("Do you want to add another item? (yes/no): ")
    
    if another_order == "cancel":
        print('\033[31m'"Your order has been canceled. Starting a new order...")
        order_total = 0  # Reset order total
        continue  # Restart the loop for a new order
    
    if another_order != "yes":
        break

print('\033[030m'f"\n     The total amount to pay is {order_total} Rs.")
print('\033[32m'" Thank you for visiting VOHRA's CAFE!".center(140))
