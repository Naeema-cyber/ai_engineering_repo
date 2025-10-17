items =["Apple", "Banana", "Orange", "Pineapple", "Kiwi"]
prices = {}

prices["Apple"] = input(f"price of {items[0]}: ")
prices["Banana"] = input(f"price of {items[1]}: ")
prices["Orange"] = input(f"price of {items[2]}: ")
prices["Pineapple"] = input(f"price of {items[3]}: ")
prices["Kiwi"] = input(f"price of {items[4]}: ")


print("Price List of Items in the Store: ")

for items, price in prices.items():
    print(f"{items}: ₦{prices}")
    
items_update = input("Item to update: ")
if items_update in prices:
    new_price = input(f"Enter the updated price for the item{items_update}: ")
    prices.update({items_update: int(new_price)})
    print(f"Updated {items_update} price to {new_price}")
else:
    print("Invalid input. price not updated.")    