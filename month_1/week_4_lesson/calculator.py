# Simple Calculator Program

# Function to add two numbers
def add(a, b):
    return a + b

# Function to subtract second number from first
def subtract(a, b):
    return a - b

# Function to multiply two numbers
def multiply(a, b):
    return a * b

# Function to divide first number by second
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: Cnnot divide by zero"
    
# Function for square root
def sqrt(a):
    if a != 0 :
        return a** 0.5
    else: return "Error: Number must not be zero"
    
# Function for exponentiation
def exp(a, b):
    return a**b

# Function for modulus
def modulus(a, b):
    return a % b

# Display operation options to the user
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Square Root")
print("6. Exponential")
print("7. Modulus")
print("8. Exit")

# Take input from the user for operation choice

# Get two numbers as input from the user

# Perform calculation based on user's choice
def main():
    try:
        while True:
            choice = int(input("Enter choice (1/2/3/4/5/6/7/8): "))
            if choice == 8:
                print("Exit")
                break
            elif choice == 5:
                num = int(input("Enter a number: "))
                print("Result: ", sqrt(num))
            else:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if choice == 1:
                    print("Result: ", add(num1, num2))
                elif choice == 2:
                    print("Result: ", subtract(num1, num2))
                elif choice == 3:
                    print("Result: ", multiply(num1, num2))
                elif choice == 4:
                    print("Result: ", divide(num1, num2))
                elif choice == 6:
                    print("Result: ", exp(num1, num2))
                elif choice == 7:
                    print("Result: ", modulus(num1, num2) )
                else: 
                    print("Invalid choice")
                
    except Exception as e:
        print("Error:", e)
    except ValueError as e:
        print("Error", e )
main()                    