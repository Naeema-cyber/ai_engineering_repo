profile = []
name = input("Enter your name: ").title()
age = int(input("Enter your age: "))
gender = input("State your gender: ").title()
profile.append(name)
profile.append(age)
profile.append(gender)
courses = []
course1 = input("Your course: ").title()
course2 = input("Enter the second course: ").title()
course3 = input("Enter the third course: ").title()
courses.append(course1)
courses.append(course2)
courses.append(course3)

print(f"\tName: {name}\n\tAge: {age}\n\tGender: {gender}\n\tCourses: {courses} ")
