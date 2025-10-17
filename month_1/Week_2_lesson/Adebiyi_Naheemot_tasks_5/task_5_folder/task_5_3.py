#3. 

user1 = input("Enter the name of a Nigerian state: ").title()
user2 = input("Enter the name of a Nigerian state: ").title()
user3 = input("Enter the name of a Nigerian state: ").title()
user4 = input("Enter the name of a Nigerian state: ").title()
user5 = input("Enter the name of a Nigerian state: ").title()

user = (user1, user2, user3, user4, user5)
if "Lagos" in user:
    print("Yes")
else:
    print("No")
    
print(len(user))