user = input("Enter a word: ")
print(len(user))

if user.isupper():
    print("The input is in upper case.")
elif user.islower():
    print("The input is in lower case.")
elif user.istitle():
    print("The input is in title case.")
else:
    print("The input contains both uppercase and lowercase.")

# reversed_str = ""
# for char in user:
#     reversed_str = char + reversed_str
# print(reversed_str)

print(user[::-1])
    