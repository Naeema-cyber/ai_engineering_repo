#11. Given "apple, banana, orange", split the string into a list of fruits.
fruits_string = "apple, banana, orange"
fruits_list = fruits_string.split()
print(fruits_list)


#12. Ask the user for a sentence and print each word on a new line.
sentence = input("Enter a sentence: ")
for char in sentence.split():
    print(char)


#13. Replace all spaces in a string with underscores.
text = "Hello! and welcome to Python programming."
new_text = text.replace(" ", "_")
print(new_text)

#14. Count how many times the letter 'a' apperars in banana.
word = "banana"
count = 0
for char in word:
    if char == 'a':
        count += 1
print(count)


#15. Check if a given string starts with "https://".
url = input("Enter a URL: ")
if url.startswith("https://"):
    print("Yes")
else:
    print("No")