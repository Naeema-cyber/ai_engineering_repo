#4. Unique Members Registration
names = input("Enter three names separated by comma: ").title()
set_of_names = set((names.split(",")))
length ={name: len(name) for name in set_of_names}
print(length)