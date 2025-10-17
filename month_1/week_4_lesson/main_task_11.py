from pathlib import Path
import csv
from participant_pkg.file_ops import save_participant, load_participant

# collecting participant details

while True:
   
   name = input("Enter participant's name: ")
   if not name.isalpha():
      print("Invalid input: Name cannot be a number, please try again.")
      continue
   try:
      age = int(input("Enter participant's age: "))
      if age <= 0:
         print("Must be a positive value.")
         continue
   except ValueError:
      print("Must be a number")
      continue
   
   phone = (input("Enter participant's phone number: "))
   if not phone.isdigit():
      print("Must be a number")
      continue
   if len(phone) != 11:
      print("Number must not exceed 11 characters! ")
      continue
   
   track = input("Enter participant's track: ")
   if not track:
      print("Track cannot be empty")
      continue
   else:
      print("Participant has been added successfully!!!")

   
   
   #Saving participant's details into the dictionary
   
   participant_dict = {
      "Name": name,
      "Age": age,
      "Phone": phone,
      "Track": track
   }
   
   save_participant(file_path, participant_dict)
   
      
      
