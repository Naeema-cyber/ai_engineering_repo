empty_set = set()
name1 = input("Enter your full name:" ).title()
if name1 in empty_set:
    print("name already entered")
else:
    empty_set.add(name1)


name2 = input("Enter your full name:" ).title()
if name2 in empty_set:
    print("name already entered")
else:
    empty_set.add(name2)

name3 = input("Enter your full name:" ).title()
if name3 in empty_set:
    print("name already entered")
else:
    empty_set.add(name3)
name4 = input("Enter your full name:" ).title()

if name4 in empty_set:
    print("name already entered")
else:
    empty_set.add(name4)

print(empty_set)

