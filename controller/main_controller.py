import os
import sys

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Get the absolute path of the project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from model.data_loader import load_crude_runs
from model.crude_run import CrudeRunRecord
from view.display_view import display_records, display_statistics
from controller.statistics_controller import calculate_statistics  # Import the function


# Correct path to the CSV file inside the 'data' folder
file_path = os.path.join(BASE_DIR, "data", "crude-runs-weekly.csv")

# Load dataset
crude_run_records = load_crude_runs(file_path)

# Display records
if crude_run_records:
    print("\nLoaded Crude Run Records:\n")
    display_records(crude_run_records[:5])  # Show first 5 records

    # Compute and display statistics
    avg_crude, max_crude, min_crude = calculate_statistics(crude_run_records)
    display_statistics(avg_crude, max_crude, min_crude)
else:
    print("\nNo records were loaded. Please check the file and try again.")
