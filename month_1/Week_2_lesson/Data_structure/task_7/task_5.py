names = ("Kola", "Tobi", "Lola")
phone_numbers = ("08012345678", "08132145678", "09012345678")
my_dict = dict(zip(names, phone_numbers))

user = input("Enter a name: ").title()
x = my_dict.get(user)
print(x)