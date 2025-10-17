#How to create a list
#method 1 using square brackets
empty_list = []
print(empty_list)

#method 2: using the list() constructor
empty_list2 = list()
print(empty_list2)


#Creating a list with initial elements.
#list of integers
numbers = [1,2,3,4,5]
print(numbers)


#list of strings
fruits = ["apple", "banana", "cherry"]
print(fruits)


#mixed data types
mixed_list = {'Alice', 25, 5.8, True}
print(mixed_list)

#Creating a list from another sequence.
#From a string (each character becomes an element)
chars = list("hello")
print(chars)


#From a tuple
my_tuple = (10,20,30)
list_from_tuple = list(my_tuple)
print(list_from_tuple)


#From a range
numbers_range = list(range(5))
print(numbers_range)


#Even numbers between 0-10
evens = [x for x in range(11) if x % 2 == 0]
print(evens)


#squares of numbers 0-4
squares = {x**2 for x in range(5)}
print(squares)


#Creating a nested list
#Matrix like list
matrix = [[1,2], [3,4], [5,6]]
print(matrix)


#Accessing elements in a nested list
print(matrix[0])
print(matrix[0][1])


#Characteristics of a list
#Ordered Collectiom

fruits = ["mango", "orange", "banana"]
print(fruits)
print(fruits[0])
print(fruits[2])


#Allows Duplicates
#List can store same value multiple times
items = ["rice", "beans", "yam", "rice"]
print(items)


#Mutable (can be changed)
numbers = [1,2,3]
numbers[1] = 20
numbers[2] = 50
print(numbers)


#Can contain different data types
mixed = [10,"Nigeria", 3.14, True]
print(mixed)


#Can be nested
#A list can contain other lists(2D or multi-dimensional lists.)
nested_list = [[1,2], ["a", "b"]]
print(nested_list)
print(nested_list[0][1])
print(nested_list[1][1])



#Dynamic Size
#You don't need to declare the size oa a list beforehand; it can grow or shrink as needed.
names = ["Ada"]
names.append("Bola")
names.append("Chidi")
names.append("Pineapple")
print(names)