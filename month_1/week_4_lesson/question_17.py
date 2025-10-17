"""
A to-do list application is a practical project that
 helps users manage tasks efficiently. This application allows
 users to add, remove, and view tasks while keeping track of
 completed and pending activities. Learning to build a to-do
 list enhances understanding of data structures, file
 handling, and basic user interaction in Python.
 This project will cover step-by-step implementation of a to
do list application, user input handling, list operations, and
 file handling for persistent storage.

 Key Concepts of To-Do List in Python
 Basic List Operations:
 -Adding tasks
 -Removing tasks
 -Marking tasks as complete
 -Displaying tasks
 -User Input Handling:
 -Using input() function
 -Handling invalid inputs
 File Handling:
 -Storing tasks in a text file
 -Retrieving saved tasks on program
 restart
 Functions in Python:
 -Defining functions for task management
 -Calling functions with user inputs
"""
# Hands-On Exercise

# Try improving the to-do list application
# with these additional features:

# 1. Save tasks to a file so that they persist after
# restarting the program.
# 2. Mark tasks as completed and display
# completed tasks separately.
# 3. Allow editing tasks instead of just adding and
# removing them.
# 4. Improve the user interface with better
# formatting and menu options.
# 5. Add a priority system to sort tasks by urgency.

# Simple To-Do List Application

# List to store tasks
tasks = []

# Function to add a task to the list
def add_task(task):
    tasks.append(task)
    print(f'Task  "{task}" has been  added successfully!')
    
# Function to edit tasks 
def edit_task(task):


# Function to remove a task from the list
def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f'Task "{task}" removed successfully!')
    else:
        print("Task not found!")

# Function to display all tasks
def view_tasks():
    if tasks:
        print("Your Tasks:")
        for y, task in enumerate(tasks, 1):  # Start numbering from 1
            print(f'{y}. {task}')
    else:
        print("No tasks in your list!")

# Infinite loop to keep the program running until user exits
while True:
    print("\nOptions: 1. Add Task  2. Remove Task  3. View Tasks  4. Save Tasks 5. Edit Tasks 6. Exit")

    # Ask user for their choice
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task: ")
        add_task(task)
    elif choice == '2':
        task = input("Enter task to remove: ")
        remove_task(task)
    elif choice == '3':
        view_tasks()
    elif choice == '4':
        task = input("Enter the task you would like to save: ")
        
    elif choice == '4':
        print("Exiting program. Have a productive day!")
        break
    else:
        print("Invalid choice! Please select a valid option.")
        