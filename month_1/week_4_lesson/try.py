# from pathlib import Path
# import csv

# my_folder = Path("new_folder")
# my_folder.mkdir(exist_ok=True)
# file_path = my_folder / "new.csv"
# file_path

# f = open(file_path, "w", encoding="utf-8")
# f.write("Hello")
# f.close()

# with open(file_path, "a", encoding="utf-8") as f:
#     f.write("\n - God help me with my exam\n")



# import time
# from tqdm import tqdm

# seconds = int(input("Enter time in seconds: "))
# # while seconds > 0:
# #     print(f"Time: {seconds} left")
# #     time.sleep(0.5)
# #     seconds -= 1
    
# # print("Time's up!\a")

# for i in tqdm(range(seconds), desc="Counting down...", total=seconds, ncols=100, ascii=True, unit="ticks"):
#     time.sleep(0.5)

import datetime

datetime.datetime.strptime()
