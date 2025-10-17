#This is a simulated USSD interface for a mobile service
print("Welcome to the Mobile Service USSD Menu.")
ussd_code = (123)
if ussd_code is (123):
    print("1. Check Balance")
    print("2. Buy Data")
    print("3. Customer Care")
    choice = input("Please enter your choice (1-3): ")
    
    if choice == '1':
        print("Your balance is $10.00")
    elif choice == '2':
        print("How much data to you intend to buy?")
        if data_amount := input("Enter amount in MB (e.g., 500 for 500MB): "):
            print(f"You have successfully purchased {data_amount}MB of data.")
    elif choice == '3':
        print("Connecting you to Customer Care...")
    else:
        print("Invalid choice. Please try again.")   