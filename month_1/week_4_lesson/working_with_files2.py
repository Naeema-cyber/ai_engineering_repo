#1. Setting up.
from pathlib import Path
import csv
import json

workspace = Path("workspace_files")
workspace.mkdir(exist_ok=True)
file_path = workspace / "notes.txt"
file_path

#2. Create file.
# (A) Create or overwrite using 'W'

f = open(file_path, "w", encoding="utf-8")
f.write("This is the first line in notes.txt\n")
f.close()


#3. Open a file
# Open for writing again(this will overwrite!)
f = open(file_path, "w", encoding="utf-8")
f.write("Replaced the old content with this line.\n")
f.close

#4. Write to a file.
f = open(file_path, "w", encoding="utf-8")
f.write("Shopping List:\n")
f.write(" - Rice\n")
f.write(" - Beans\n")
f.write(" - Garri\n")
f.close()

#5. Append to a file
# Append adds to the end without deleting what's already there.
f = open(file_path, "a", encoding="utf-8")
f.write(" - Groundnut oil\n")
f.write(" - Maggi\n")
f.close()

#6. Read from a file
#Read the whole file
f = open(file_path, "r", encoding="utf-8")
content = f.read()
print(content)

#Read line-by-line
f = open(file_path, "r", encoding="utf-8")
print("First line:", f.readline().rstrip())
print("Second line:", f.readline().strip())
f.close()

#Read as a list of lines
f = open(file_path, "r", encoding="utf-8")
lines = f.readlines()
f.close()
print("Lines list:", [line.rstrip() for line in lines])


#Iterate over lines (memory-friendly)
f = open(file_path, "r", encoding="utf-8")
for line in f:
    print("->", line.rstrip())
f.close()

#7. Close the file
f.close()  #Closes the file.

#8. Use with open(...) as f: (best practice)
#Write safely
with open(file_path, "w", encoding="utf-8") as f:
    f.write("My Todo List:\n")
    f.write(" - Revise Python file handling\n")
    f.write(" - Practice error handling within a function")
    f.write(" - Practice JSON & CSV\n")
    
#Append safely
with open(file_path, "a", encoding="utf-8") as f:
    f.write(" - Build a small project\n")
    
#How to manage error
from pathlib import Path

workspace = Path("workspace_files")
workspace.mkdir(exist_ok=True)

# Try to read a file that doesn't exist
try:
    with open(workspace / "missing_file.txt", "r") as f:
        content = f.read()
        print("File content:", content)
except FileNotFoundError:
    print("Oops! That file doesn't exist yet.")
    print("Let's create it first!")
    
# Now create the file
with open(workspace / "missing_file.txt", "w") as f:
    f.write("Now I exist!")
    print("File created successfully!")
    
    
# If you write this correctly, you should see something like this...
""""
Oops! That file doesn't exist yet.
Let's create it first!
File created successfully!
"""

#Checking if the file exist before using them.


workspace = Path("workspace_files")
file_path = workspace / "notes.txt"

# Check if our file exists
if file_path.exists():
    print(f"Found the file: {file_path.name}")
    
    # Get some information about the file
    file_size = file_path.stat().st_size
    print(f"File size: {file_size} bytes")
    
    # Read and show the content
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        print(f'Content preview: {content[:50]}...') # First 50 characters
else:
    print(f"File {file_path.name} doesn't exist")
    print("You might want to create it first!")


# Working with JSON Files

workspace = Path("workspace_files")

# Create some student data (like a mini database)
student_data = {
    "name": "Oyindamola",
    "age": 16,
    "courses": ['Python', "Data Science", "Web Development"],
    "grades": {"Python": "A", "Data Science": "B+", "Web Development": "A-"},
    "is_graduated": False
}

# Save the data to a JSON file
json_file = workspace / "student_data.json"
with open(json_file, "w", encoding="utf-8") as f:
    json.dump(student_data, f, indent=2) # indent=2 makes it pretty and readable.
print("student_data saved to JSON# file!")

# Now read it back
with open(json_file, "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
    
print("\nData read from JSON file:")
print(f"Student name: {loaded_data['name']}")
print(f"Age: {loaded_data['age']}")
print(f"Courses: {','.join(loaded_data['courses'])}")
print(f"Python grade: {loaded_data['grades']['Python']}")



#Working with CSV files

workspace = Path("workspace_files")
csv_file = workspace / "students.csv"

# Create sample student data
student = [
    ["Name", "Age", "Course", "Grade"], # Header row
    ["Precious", 20, "Python", "A"],
    ["Favour", 22, "Javascript", "B+"],
    ["Ore", 21, "Python", "A-"],
    ["Susan", 23, "Data Science", "A"]
]

