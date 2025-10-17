#Creating Tuples
#Using parenthesis()
#Example1: tuple with multiple items
fruits = ("apple", "banana", "cherry")
print(fruits)


#Without parenthesis (tuple packing)
numbers = 1,2,3
print(numbers)


#Single_item tuple (must include a comma)
single_item = ("apple",)
print(single_item)
print(type(single_item))

#Using the tupple()constructor
fruits_list = ["apple", "banana", "cherry"]
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)


#Ordered
colors = ("red", "green", "blue")
print(colors[0])


#Immutable ( uncomment and run. This will cause an error)
colors[1]

#Allow duplicates
numbers = (1,2,2,3)
print(numbers)


#Mixed data types
mixed = ("apple", 3, True, 5.6)
print(mixed)


#Nested tuples
nested = (("a", "b"), (1,2))
print(nested)


#Tuple Operations

#1. Indexing

fruits = ("apple","banana", "cherry")
print(fruits[1])
print(fruits[-1])
print(fruits[-3])


#2. Slicing

print(fruits[0:2])
print(fruits[::-1])


#3. Concatenation

tuple1 = (1,2)
tuple2 = (3,4)
result = tuple1 + tuple2
print(result)


#4. Repetition
nums = (1,2)
print(nums * 3)

#5. Membership

fruits = ("apple", "banana", "cherry")
print("banana" in fruits)
print("grape" not in fruits)

#6. Iteration
for fruit in fruits:
    print(fruit)


#Working with Tuples
#Unpacking Tuples
person = ("John", 25, "Nigeria")
name, age, country = person
print(name)
print(age)
print(country)


#Tuple methods
#dot count() and dot index()

numbers = (1,2,2,3,4)
print(numbers.count(2)) #counts the occurrences of 2
print(numbers.index(3)) #position of first occurrence of 3


#Converting between list and tuple

#Tuple to List
t = (1,2,3)
lst = (list(t))
lst.append(4)
print(lst)


#List back to tUPLE
t = tuple(lst)
print(t)


#built-in functions with Tuples
nums = (4,1,7,3)
print(len(nums))
print(max(nums))
print(min(nums))
print(sum(nums))