#1. Write a program to take a string input from the user and display it in uppercase.
name = input("Enter your name: ").upper()
print(name)


#2. Given the string "python", print its first and last characters
nam = "python"
print(nam[0])
print(nam[-1])


#3. Ask the user for their name and print "hello,!" where is the user's input.
user = input("Enter your name: ").title()
print(f"Hello! {user}")


#4. Write a program to count the number of characters in a string without using len()
word = "underscore"
count = 0
for char in word:
    count += 1
print(count)


#5. Given "Hello World", replace "World" with "Python"
text = "Hello World"
new_text = text.replace("World", "Python")
print(new_text)