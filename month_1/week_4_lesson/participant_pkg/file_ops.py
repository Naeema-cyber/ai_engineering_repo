import csv
from pathlib import Path

header = ["Name","Age", "Phone", "Track"]

def save_participant(file_path, participant_dict):
    file = Path(file_path)
    if not file.exist() or file.stat().st_size == 0:
            writer.writeheader()
            
    with open(file, "a", encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=header)
    writer.writerow(participant_dict)
        
        
        
        
def load_participant(file_path):
    file = Path(file_path)
    if not file.exists():
        print("file does not exist")
    else:
        print(f"Loading participants from {file.name}")
        with open(file, mode="r", newline="", encoding="utf-8") as f:
            print(f.read())