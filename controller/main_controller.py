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

# Display records
if crude_run_records:
    print("\nLoaded Crude Run Records:\n")
    for record in crude_run_records[:5]:  # Display first 5 records
        print(record)
else:
    print("\nNo records were loaded. Please check the file and try again.")


