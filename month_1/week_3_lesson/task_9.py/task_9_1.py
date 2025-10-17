#1. Simulated ussd menu interaction
#This is a simulated ussd interface for a mobile service:

print("Welcome, how can we be of service today?")
ussd_code = (310)
if ussd_code is (310):
    print("1. Data plans")
    print("2. Check Balance")
    print("3. Customer Care")
    choice = int(input("please enter your choice: "))
    
    
    if choice == '1':
        print("Your balance is #10,000")
    elif choice == '2':
        print("1. 500mb")
        print("2. 1000mb")
        choices = int(input("Please enter 1 of the two choices provided above: "))
        if choices == '1':
            print("You have successfully purchased 500mb of data")
        elif choices == '2':
            print("You have successfully purchaes 1000mb of data")
        else:
            print("Invalid choice")
    elif choice =='3':
        print("Connecting you to a customer care representative..")
    else:
        print("Invalid choice. Please try again later.")
        