def greet(name):
    print("Hello", name, "welcome to AI Fellowship!")

#Calling with parameter- the actual name
greet("Class rep")
greet("Ridwan")

#Function call
result = greet("Esther")
#You will notice that it did not store the name
print("Result:", result)



def add(a, b):
    return a + b

#Function call

result = add(4, 6)
print("The sum is:", result)


def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1
#using the generator
for number in count_up_to(5):
    print(number)

def introduce(name, track):
    print("My name is", name)
    print("I am learning", track, ".")
#function call
introduce("Ngozi", "AI Engineering")

# Change the arrangement and watch the output
introduce("AI Engineering", "Ngozi")


def introduce(name, track):
    print("My name is", name)
    print("I am learning", track,".")

# function call
introduce(name = "Ngozi", track = "AI Engineering")

# change the argument and watch the output

introduce(track = "AI Engineering", name = "Ngozi")

def introduce(name, track = "AI Engineering"):
    print("My name is", name)
    print("I am learning", track,".")

# function call
# Without specifying the default argument, but watch the ouput
introduce("Paul")  

# Specify the default argument and watch the output

introduce("Tunji Paul", track = "AI Development")


def add_numbers(*args):
    total = 0
    for num in args:
        total += num
    print("Sum:", total)

# function call 
# Take note of the output
add_numbers(2, 4, 6)
add_numbers(10, 20, 30, 40, 50)


def student_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


# function call - Take note of the output
student_details(name="Peter", track = "AI Engineering", interest="Block Chain")


# Define student profile function

# Ensure to note the order of arrangement of the types of arguments used.
# This is how to arrange it of you are using everything or some of them together

def participant_profile(name, age, track="AI Development", *skills, **extra_info):
    """
    Generate a profile for a bootcamp participant using different types of arguments.
    """
    profile = f"\n--- Bootcamp Participant Profile ---\n"
    profile += f"Name: {name}\n"
    profile += f"Age: {age}\n"
    profile += f"Track: {track}\n"

    # Skills (from *args)
    if skills:
        profile += "Skills: " + ", ".join(skills) + "\n"
    else:
        profile += "Skills: Not yet specified\n"

    # Extra info (from **kwargs)
    if extra_info:
        profile += "Additional Info:\n"
        for key, value in extra_info.items():
            profile += f" - {key.capitalize()}: {value}\n"

    return profile  # Do you remember `return` and why it is used? We are using it so it can be reused in other places


# ---------- LEts test ----------

# Example 1: Using only positional arguments
print(participant_profile("Peter", 24))

# Example 2: Adding keyword/default argument
print(participant_profile("Ridwan", 29, track="AI Engineering"))

# Example 3: Adding variable-length positional arguments (*args)
print(participant_profile("David", 27, "Data Science", "Python", "SQL", "Machine Learning"))


# Example 4: Adding variable-length keyword arguments (**kwargs)
print(participant_profile(
    "Sophia", 30, "Cybersecurity",
    "Networking", "Ethical Hacking", "Python",
    interest="Blockchain", city="Shagamu", phone="08123456789"
))