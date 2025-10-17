# Days and Activities pairing
days_of_the_week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")

activity_1 = input("Enter the activity for Monday: ")
activity_2 = input("Enter activities for Wednesday: ")
activity_3 = input("Enter the activites for Friday: ")
activities = (activity_1, activity_2, activity_3)

weekly_activites = {
    "Sunday": "No activity",
    "Monday":  activity_1,
    "Tuesday": "No activity",
    "Wednesday": activity_2,
    "Thursday": "No activity",
    "Friday": activity_3,
    "Saturday": "No activity"
}

for key, value in weekly_activites.items():
    print(f"{key}: {value}")
    
print("\nWeekly Activities.")
daily_activities = dict(zip(days_of_the_week, activities))
print(daily_activities)
