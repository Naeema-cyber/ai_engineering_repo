"""This code explains the key processes involved in obtaining a federal government scholarship. If all conditins are met then the applicant will bw qualified for the scholarship but if not the applicant will be disqualified_summary_
    """

name = input("Enter your name: ").upper()
age = int(input("Enter your age: "))
enrollment = input("Are you an undergraduate: ").upper()
other = input("Are you a beneficiary of another scholarship currently?").upper()
subjects = input("Enter 5 relevant subjects separated by comma: ")
dict = {
    "A": 15,
    "B":12,
    "C": 9,
    "D": 6,
    "E": 3,
    "F": 0
}           
print(dict)
grade = int(input("Enter the sum of your grade for 5 relevant subject: "))


 

eligibility = (age < 18) and (enrollment == "YES") and (other == "NO") and (grade >= 60)

print(f"Candidate: {name}\nAge: {age}\nGrade: {grade}\nEligible: {eligibility}")