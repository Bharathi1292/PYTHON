import csv
import json

def test_csv_columns():
    with open('profiles.csv', 'r') as f:
        reader = csv.reader(f)
        header = next(reader)
        assert len(header) == 12

def test_csv_rows():
    with open('profiles.csv', 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
        assert len(rows) > 900

def test_json_properties():
    with open('data.json', 'r') as f:
        profiles = json.load(f)
        for profile in profiles:
            assert 'property1' in profile
            assert 'property2' in profile
            # Fortsätt med resterande properties

def test_json_rows():
    with open('data.json', 'r') as f:
        profiles = json.load(f)
        assert len(profiles) > 900