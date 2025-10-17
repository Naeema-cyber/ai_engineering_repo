#  Creating unique voters registration system

voter_names = set()
#  implementing loop
for voter in range(5):
    voter_name = input("Kindly enter your name: ")
    
    list_voter = list(voter_names)
    for name in range(len(voter_names)):
        if voter_name == list_voter[name]:
            print(f"{voter_name} is trying to register twice, while it is not allowed, the name won't be added to the list")
    voter_names.add(voter_name)
    
print(f"The total number of unique voters that registered is {len(voter_names)}")