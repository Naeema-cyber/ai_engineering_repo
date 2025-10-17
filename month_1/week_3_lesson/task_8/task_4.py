student = {}
name = str(input("Enter your name: "))
age = int(input("Enter your age: "))
scores = [70, 85, 90]

student.update({"Name": name})
student.update({"Age": age})
student.update({"Scores": scores})

avg_score = (scores[0] + scores[1] + scores[2])/ 4
student["passed"] = avg_score>=50

teenager = (student["Age"] >= 13) and (student['Age'] <= 19)

print(f"student:\n Name: {student['Name']} \n Age: {student['Age']}\n Scores:{student["Scores"]}\n Passed:{student['passed']}\nTeenager:{teenager}")