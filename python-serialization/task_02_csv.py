import csv
import json

def convert_csv_to_json(csv_file):
    try:
        with open(csv_file, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            data = [row for row in reader]

        with open('data.json', 'w') as jsonfile:
            json.dump(data, jsonfile, indent=4)
                
        return True
    except FileNotFoundError:
        return False
