amount = float(input("Enter the amount: "))
dollar_rate = float(1535.56)
pounds_rate = float(2063.43)

dollar_to_naira_rate = amount * dollar_rate
pounds_to_naira_rate = amount * pounds_rate

print(f"{dollar_to_naira_rate:,}\n{pounds_to_naira_rate:,.2f}")