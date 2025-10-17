#range()
for i in range(3):
    print(i)


#zip()
names = ["Esther", "Precious", "Kennie"]
scores = [85, 90,75]
for n, s in zip(names, scores):
    print(n, "Scored", s)


#map()
nums = [1,2,3,4]
squared = list(map(lambda x: x**2, nums))
print(squared)


#filter()
even_nums = list(filter(lambda x: x % 2 == 0, nums))
print(even_nums)


#Student Performance & Feedback System

#Step 1: Input Student data
name1 = input("Enter first student name: ")
score1 = int(input("Enter score for " + name1 +": "))

name2 = input("Enter second student name: ")
score2 = int(input("Enter score for " + name2 + ": "))

name3 = input("Enter third student name: ")
score3 = int(input("Enter score for " + name3 + ": "))

# step 2: Store in lists
names = [name1, name2, name3]
scores = [score1, score2, score3]

# Step 3: Display data
print("\nStudent Data:")
for index, (n, s) in enumerate(zip(names, scores)):
    print(f"{index + 1}. {n} - {s}")

# Step 4: Summary using built-ins
total = sum(scores)
average = round(total / len(scores), 2)
highest = max(scores)
lowest = min(scores)

print("n\Performance Summary")
print("Total Score:", total)
print("Average Score:", average)
print("Highest Score:", highest)
print("Lowest Score:", lowest)

#Step 5: Ranking(using sorted and zip)
ranked = sorted(zip(scores, names), reverse=True)
print("\nRanking:")
for rank, (score, name) in enumerate(ranked, 1):
    print(f"{rank}. {name} - {score}")


# Step 6: Check data types
print("\nData Type Checks:")
print("Type of names:", type(names))
print("Type of scores:", type(scores))
print("ID of names list:", id(names))
print("ID of scores list:", id(scores))


# Step 7: Filter passing students (>=50)
passing = list(filter(lambda s: s >= 50, scores))
print("\nPassing Scores:", passing)


#Step 8: Map names to uppercase
upper_names = list(map(lambda n: n.upper(), names))
print("Uppercase Names:", upper_names)

#Step 9: Use help() to show documentation of len
print ("\nHelp on len():")
help(len)