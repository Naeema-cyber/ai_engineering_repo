#6. Attendance tracker
days_of_the_week = []
months_of_the_year = []
student_name = input("Enter your name: ").title()
gender = input("Enter your gender: ").title()
track = input("Enter your track: ").title()
current_month_number = int(input("Enter the equivalent number of the current month: "))
current_day_number = int(input("Enter the current day number : "))

days_of_the_week.append(current_day_number)
months_of_the_year.append(current_month_number)

days_of_the_week_tuple = tuple(days_of_the_week)
months_of_the_year_tuple = tuple(months_of_the_year)

print(f"{"Name:", student_name}\n{"Gender:", gender}\n{"Track:", track}\n{"Day of the week:", days_of_the_week_tuple}\n{"Month of the year:", months_of_the_year_tuple}")