import csv
from model.crude_run import CrudeRunRecord  # Ensure correct import

def load_crude_runs(file_path: str):
    """
    Reads a CSV file and initializes CrudeRunRecord objects.
    """
    records = []
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                try:
                    date = row['Week End']
                    crude_runs = float(row['Crude Volumes For The Week'])
                    records.append(CrudeRunRecord(date, crude_runs))
                except KeyError as e:
                    print(f"Skipping row due to missing key: {e}")
                except ValueError as e:
                    print(f"Skipping row due to value error: {e}")
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except Exception as e:
        print(f"Unexpected error: {e}")

    return records


def save_crude_runs(file_path, records):
    fieldnames = ["Week End", "Crude Volumes For The Week"]
    
    try:
        with open(file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for record in records:
                writer.writerow({"Week End": record.date, "Crude Volumes For The Week": record.crude_runs})
        print("Data successfully saved to file.")
    except Exception as e:
        print(f"Error saving data: {e}")
