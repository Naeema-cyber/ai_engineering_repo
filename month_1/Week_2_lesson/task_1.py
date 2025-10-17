#1. Your favourite life quote.

user = input("Enter your favourite life quote: ").title()
print(f"\"{user}\"")


#2. Shopping list manager
empty_list = []
items = input("Enter items separated by comma: ").split()
for item in items:
    empty_list.append(item)
print(empty_list)

