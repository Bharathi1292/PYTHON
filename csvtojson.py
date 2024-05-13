import csv
import json

def csv_to_json(csv_file, json_file):
    
    with open(csv_file, 'r') as csv_file:
        
        csv_reader = csv.DictReader(csv_file)
        data = list(csv_reader)
    
    with open(json_file, 'w') as json_file:
        json_file.write(json.dumps(data, indent=4))

# Example usage
csv_to_json('profiles1.csv', 'movies.json')
