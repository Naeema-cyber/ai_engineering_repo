#CREATING DICTIONARIES

#1.  Using curly braces

student = {
    "name": "Ada",
    "age": 20,
    "course": "computer Science"
}

print(student)


#2. Using the dict() constructor

student_info = dict(name="John", age=25, course="Maths")
print(student_info)



#Empty dictionary

empty_dict = {}
print(empty_dict)



#DICTIONARY COMPREHENSION

#Syntax:

#Create a dictionary of numbers and their squares
squares = {x: x**2 for x in range(1, 6)}
print(squares)

#With Condition

#Create a dictionary of even numbers and their cubes
evens_cube = {x: x**3 for x in range(1, 10) if x % 2 == 0}
print(evens_cube)


#From Existing Dictionary

students = {"Ada": 85, "John": 40, "Musa": 65}
 #Filter students who passed (score >=50)
passed_students = {name: score for name, score in students.items() if score >=50}
print(passed_students)


#Using String Keys

names = ["Ada", "John", "Musa" ,"Jimoh"]
lengths = {name: len(name) for name in names}
print(lengths)



#Accessing Dictionary Items
#Define a dictionary
student = {"name": "Ada", "age": 20, "course": "computer science"}


#Using key
print(student["name"])

#Using get() method (avoids error if key is missing)
print(student.get("age"))
print(student.get("grade", "Not Found"))

#Modifying Dictionaries
student["age"] = 21 #change value 
student["grade"] = "A"  # Add new key-value pair
print(student)


#rEMOVING ITEMS FROM DICTIONARIES
#1. using pop()
student.pop("grade")
print(student)

#2. using popitem() ----removes last inserted key-value
#del student.popitem()

#3. Using del keyword
del student["course"]
print(student)


#Using clear()---- removes all items
student.clear()

print(student)



#Dictionary methods
#dot keys(), dot values(), dot items(), dot update()

person = {"name": "Emeka", "age": 30}
#1. keys()
print(person.keys())

#2. values()
print(person.values())

#3. items()
print(person.items())


#4. .Update()
person.update({"age": 31, "city": "Lagos"})
print(person)



#Nested Dictionaries

students = {
    "student1": {"name": "Ada", "age": 20},
    "student2": {"name": "John", "age": 22},

}

print(students["student1"]["name"]) #Access nested data


#Looping through dictionaries
#Define a dictionary
student = {"name": "Ada", "age": 20, "course": "computer science"}

#Loop through keys
for key in student:
    print(key)


#Loop through values
for value in student.values():
    print(value)


#Loop through key-value pairs

for key, value in student.items():
    print(f"{key}: {value}")


#Storing a student's biodata
student = {
    "name": "Chinedu",
    "age": 19,
    "department": "Engineering",
    "subjects": ["Maths", "Physics", "Chemistry"],
    "is_full-time": True
}

print(f"Name: {student['name']}")
print(f"subjects: {','.join(student['subjects'])}")