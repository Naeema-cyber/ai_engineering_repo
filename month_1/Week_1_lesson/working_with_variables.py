# Define a variable using int., float and strings
# Full_name = ("Adebiyi Naheemot Adenike") # string variable
# Age = 20 #integer
# value_of_pi = 3.14

# print(Full_name)
# print(Age)
# print(value_of_pi)



# int() #This is an integer function
# float()
# str()
# bool()


#convert input to integer
age = int(input("Enter your age: "))
print(f"You will be {age + 1} years old next year.")


#Task: create a ussd code scenario where you can select one or more options
#step1: create 2 options to choose from
#step2: Amount to recharge or transfer
#step3: Phone number or account number


print("Welcome to Swiss Bank!, how can we be of service today?")
request1 = input("Recharge or Transfer?")
print(request1)
request2 = input("Amount to recharge or Account number to transfer to.")
print("Please hold on while we process your transaction!!!")
request3 = input("Enter your transaction pin")
print("..............Request processing.........")

print("Transaction successful!!!!😍😍😍")

