# test_data.py

import pytest
import csv
import json

# Function to read data from CSV file
def read_csv(profiles):
    data = []
    with open(profiles, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(profiles)
        for row in reader:
            data.append(row)
    return data

# Function to read data from JSON file
def read_json(data):
    with open(data, 'r', encoding='utf-8') as file:
        data = json.load(data)
    return data

# Test to verify CSV file contains 12 columns
def test_csv_columns():
    data = read_csv('profiles1.csv')
    assert len(data[0]) == 12

# Test to verify CSV file contains 900+ rows
def test_csv_rows():
    data = read_csv('profiles1.csv')
    assert len(data) >= 900

# Test to verify JSON file contains all required properties
def test_json_properties():
    data = read_json('data.json')
    assert all(key in data[0] for key in ['Givenname', 'Surname', 'Streetaddress', 'City',  'Zipcode', 'Country','CountryCode', 'NationalId', 'TelephoneCountryCode', 'Telephone', 'Birthday', 'ConsentToContact'])

# Test to verify JSON file contains 900+ rows
def test_json_rows():
    data = read_json('data.json')
    assert len(data) >= 900
