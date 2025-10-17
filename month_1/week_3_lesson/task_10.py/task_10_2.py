# A dictionary called store with items and their available quantities.
store = {"Marker": 30, "Ruler": 20, "Pencil": 400, "Crayon": 10, "Book": 50}

print(f"These are the list of items available in Rhema stores: {store}")

while True:
    try:
        # Take the user input
        item = input("Kindly enter the item you want to buy from the list above (or type 'exit' to quit): ").title()

        # Exit condition
        if item.lower() == "exit":
            print("Thank you for shopping with us. Have a lovely day!")
            break  

    
        if item not in store:
            print(f"Sorry, {item} is not available at the moment.")

        elif store[item] == 0:
            print(f"Sorry, {item} is out of stock.")

        else:
            quantity = int(input(f"Kindly enter the quantity of {item} you want to buy: "))
            
            if quantity <= 0:
                print("Quantity must be greater than zero.")


            else:

                # Remove purchased quantity from stock
                store[item] -= quantity

                # Confirm successful purchase
                print(f"Congratulations! You successfully purchaed {quantity} {item}(s).")

    except ValueError:
        print("Invalid input! Please enter numbers only for quantity.")
    except Exception:
        print("An unexpected error occurred:")
    finally:
        print("Transaction completed.")