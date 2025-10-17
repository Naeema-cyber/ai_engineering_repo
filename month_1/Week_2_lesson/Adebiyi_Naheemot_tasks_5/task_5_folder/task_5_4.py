#4. Tuple unpacking
name = input("Enter your name: ").title()
age = int(input("Enter your age: "))
favourite_color = input("Enter your favourite color: ").title()
home_town = input("Enter your home town: ").title()
profiles = (name, age, favourite_color, home_town)

# for profile in profiles:
#     print(profile)

print(f"Name: {name}\nAge: {age}\nFavourite Color: {favourite_color}\nHome Town: {home_town}")