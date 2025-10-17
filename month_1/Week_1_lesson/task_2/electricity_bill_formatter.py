name = input("Enter your full name: ").upper()
unit = int(input("How much units do you consume daily? "))
cost = 6.78
total_cost = unit * cost

print(f"Name:{name}\nUnit: {unit}\nCost: {cost}\nTotal: {total_cost:.2f}")