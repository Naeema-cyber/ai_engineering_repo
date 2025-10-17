#single quotes 
name = 'Ada'
print(name)

#double quotes
greeting = "Hello"
print(greeting)

#triple quotes (for multi-line strings)
story = '''Once upon a time, 
there was a coder name Ada.'''
print(story)


#string with numbers and symbols
password = "p@ssword123" 
print(password)


#indexing
word = "python" 
print(word[0])
print(word[-1])


#slicing
word = "python"
print(word[0:4])
print(word[2:])
print(word[:3])
print(word[::2])
print(word[::-1])


#concatenation
a = "Hello"
b = "World"
print(a + " " + b)


#repetition
word = "Hi! "
print(word * 3)


#membership
text = "python programming"
print("python" in text)
print("Java" not in text)

#find() /  rfind()

text = "Hello World"
print(text.find("o"))

#startswith() / endswith()
filename = "data.csv"
print(filename.startswith("data"))
print(filename.endswith(".csv"))


