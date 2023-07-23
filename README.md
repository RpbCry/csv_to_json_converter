# CSV to JSON Converter

## Description
This Python script converts data from a CSV (Comma-Separated Values) file to a JSON (JavaScript Object Notation) file. The script uses the `csv` module to read the data from the CSV file and the `json` module to write it to a JSON file.

## Usage
1. Ensure you have Python installed on your system (Python 3.6 or later).
2. Place the CSV file (`data.csv`) that you want to convert in the same directory as the `csv_to_json_converter.py` script.
3. Run the script using the following command:
python csv_to_json_converter.py
After running the script, a new file named `data.json` will be created in the same directory, containing the JSON representation of the data from the CSV file.

## Input CSV Format
The input CSV file (`data.csv`) should have a header row that specifies the column names, and subsequent rows should contain the corresponding data. Each row in the CSV file will be converted to a JSON object in the output JSON file.

## Output JSON Format
The output JSON file (`data.json`) will contain an array of JSON objects, where each object represents a row from the input CSV file. The keys in the JSON objects will correspond to the column names from the CSV header row, and the values will be the data from the respective rows.

## Example
Suppose we have a CSV file named `data.csv` with the following contents:
Name,Age,Email
John,30,john@example.com
Jane,25,jane@example.com
Running the script with this CSV file will create a new file named `data.json` with the following JSON content:

```json
[
    {
        "Name": "John",
        "Age": "30",
        "Email": "john@example.com"
    },
    {
        "Name": "Jane",
        "Age": "25",
        "Email": "jane@example.com"
    }
]

## Acknowledgments
The script was created by Rpbcry as a helpful utility for converting CSV data to JSON format.
If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.
Happy coding!



