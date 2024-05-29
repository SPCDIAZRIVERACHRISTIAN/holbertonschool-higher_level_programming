import csv
import json

def convert_csv_to_json(csv_file):
    data = []
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            try:
                data.append(dict(row))
                json.dumps(data)
                return True
            except FileNotFoundError as e:
                print(f"Error: {e}")
                return False