import csv
import json

def csv_to_json(csv_file, json_file):
    # Open the CSV file with specified encoding
    with open(csv_file, 'r', encoding='utf-8') as csv_file:
        # Read the CSV file using csv.DictReader
        csv_reader = csv.DictReader(csv_file)
        
        # Convert the CSV data to a list of dictionaries
        data = list(csv_reader)
    
    # Write the data to a JSON file
    with open(json_file, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

# Example usage
csv_to_json('profiles1.csv', 'data.json')

