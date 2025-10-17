name = input("Name of your school: ").title()
tuition = float(input("How much is your school fee? ₦"))
hostel = float(input("How much is your hostel fee? ₦"))
feeding = float(input("How much is your feeding cost? ₦"))
total = tuition + hostel + feeding 
print(f"{name}\n₦{total}")