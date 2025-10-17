#6. Check if a given string contains the substring "python" (case -insensitive)
given_string = input("Enter a string: ").lower()
if "python" in given_string:
    print("Yes")
else:
    print("No")


#7. Write a program to reverse a string without using slicing.
reversal = input("Enter a string to reverse: ")
reversed_string = ""
for char in reversal:
    reversed_string = char + reversed_string
print(reversed_string)


#8. Given a string with extra spaces at the beginning and end, remove those spaces.
string_with_spaces = "     Hello, World!     "
new_string = string_with_spaces.strip()
print(new_string)


#9. Ask the user to enter a sentence and print the number of vowels in it.
sentence = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
count = 0
for char in sentence:
    if char in vowels:
        count += 1
print(f"Number of vowels: {count}")


#10. Convert a string "1234" to an integer and multiply by 2.
number = "1234"
result = int(number) * 2
print(result)