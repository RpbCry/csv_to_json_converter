import csv
import json

def convert_csv_to_json(csv_file, json_file):
    data = []
    with open(csv_file, 'r', newline='', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            data.append(row)

    with open(json_file, 'w', encoding='utf-8') as jsonfile:
        json.dump(data, jsonfile, indent=4)

if __name__ == "__main__":
    csv_file = "data.csv"
    json_file = "data.json"
    convert_csv_to_json(csv_file, json_file)
