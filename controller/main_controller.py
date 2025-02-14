# controller/main_controller.py

import os
import sys

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from model.data_loader import load_crude_runs
from model.crude_run import CrudeRunRecord

# Get the absolute path of the project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Correct path to the CSV file inside the 'data' folder
file_path = os.path.join(BASE_DIR, "data", "crude-runs-weekly.csv")

# Load dataset
crude_run_records = load_crude_runs(file_path)

def calculate_statistics(records):
    """
    Calculate statistics for crude run records.
    Returns the average, max, and min crude run values.
    """
    if not records:
        return None, None, None
    
    crude_values = [record.crude_runs for record in records]
    avg_crude = sum(crude_values) / len(crude_values)
    max_crude = max(crude_values)
    min_crude = min(crude_values)

    return avg_crude, max_crude, min_crude

# Calculate statistics
avg_crude, max_crude, min_crude = calculate_statistics(crude_run_records)

# Display statistics
if avg_crude is not None:
    print(f"\nStatistics:")
    print(f"Average Crude Runs: {avg_crude:.2f} Thousand Cubic Meters per Day")
    print(f"Max Crude Runs: {max_crude:.2f} Thousand Cubic Meters per Day")
    print(f"Min Crude Runs: {min_crude:.2f} Thousand Cubic Meters per Day")



# Display records
if crude_run_records:
    print("\nLoaded Crude Run Records:\n")
    for record in crude_run_records[:5]:  # Display first 5 records
        print(record)
else:
    print("\nNo records were loaded. Please check the file and try again.")


