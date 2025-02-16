import csv
import uuid
import os
import sys

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from model.crude_run import CrudeRunRecord

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


import os
import csv
import uuid

def save_crude_runs(crude_run_records):
    """Save crude run data to a new CSV file with a UUID-based name."""
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_dir = os.path.join(BASE_DIR, "data")
    os.makedirs(data_dir, exist_ok=True)  # Ensure data folder exists

    # Generate unique filename
    filename = f"crude-runs-{uuid.uuid4().hex[:8]}.csv"  # Short UUID
    file_path = os.path.join(data_dir, filename)

    # Write data to file
    try:
        with open(file_path, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Crude Volume"])  # CSV Header
            for record in crude_run_records:
                writer.writerow([record.date, getattr(record, 'crude_volume', getattr(record, 'volume', None))])  
        print(f"Data saved successfully as {filename}")
    except Exception as e:
        print(f"Error saving file: {e}")
