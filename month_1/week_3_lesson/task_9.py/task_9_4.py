#  Simulate a football match ticket system

seat_number = set(range(1,51))
print(seat_number)

#seat_number = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50}
booked = []
for booked_seat in range(5):
    user_booked_seat = int(input("Kindly book a seat by choosing (1 - 51): "))
    if user_booked_seat >= 51:
        print(f"{user_booked_seat} is out of range from the seat number. Try again.")
    else:
        confirm_seat = seat_number.discard(user_booked_seat)
        if user_booked_seat in booked:
            print("The seat has booked already!")
        else:
            booked.append(user_booked_seat)
            print(f"The remaining seats after you booked is {seat_number}")
        




