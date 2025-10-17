#Task3:Word Counter

ask = input("Write a sentence: ").split(" ")
print(len(list(ask)))


#Task 4: Name organizer
name = input("Enter 5 names separated by space: ")
new_name = name.lower().split(" ")
new_name.sort()
print(new_name)

[print(f"{n}") for n in new_name]
