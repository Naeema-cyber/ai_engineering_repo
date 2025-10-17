#Basic usage of input()
name = input("Enter your name: ")
print("Hello," , name)

# step1; create a variable
# step2; print a welcome statement in the form of a string and the variable
# step3; create the first input variable
# step4; create the second input variable
# step5; print the first and second order
name = input("Enter your name: ")
print("Welcome to our Restaurant," , name)
order1 = input("What would you like to order from us today?")
order2 = input("Anything else you'd like to add?" )
print(f"Your {order1} and {order2} is coming right up")



#Convert input to integer
age = int(input("Enter your age: "))
print(f"You will be {age + 1} years old next year.")

# Calculator using input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum_result = num1 + num2
print(f"The sum of {num1} and {num2} is {sum_result}.")

