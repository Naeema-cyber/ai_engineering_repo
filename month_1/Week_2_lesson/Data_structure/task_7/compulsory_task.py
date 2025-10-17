subjects = ("Maths", "English", "Chemistry")
print(subjects)
name = input("Enter your name: ").title()
age = int(input("Enter your age: "))
gender = input("Enter your gender: ").title()
scores = input("Enter your scores for the equivalent subjects separated by comma: ").split(", ")
guardian_name = input("Enter your guardian's name: ").title()
guardian_phone = input("Enter your guardian's phone number: ")
hobbies = set(input("Enter your hobby(ies) if you have more than one separated by comma: ").title().split(","))
print(scores)
set_of_scores = tuple(scores)
print(set_of_scores)

average_score = sum(set_of_scores) / len(set_of_scores)
print(average_score)
academic_scores = dict(zip(subjects, set_of_scores))
print(academic_scores)
# guardian_info = dict(zip(guardian_name, guardian_phone))

student_info = {}
student_details = {}
guardian_info = {}

student_details["Name"] = name
student_details["Age"] = age
student_details["Gender"] = gender
student_details["Hobbies"] = hobbies

guardian_info["Guardian Name"] = guardian_name
guardian_info["Guardian Phone No"] = guardian_phone

student_info["Student Details"] = student_details
student_info["Average Score"] = float(f"{average_score:.2f}")
student_info["Academic Scores"] = academic_scores
student_info["Guardian Info"] = guardian_info



print(f"\nThis is the profile of {name}.\n {student_info}")

