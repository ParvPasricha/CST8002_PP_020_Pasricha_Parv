import os
import sys

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Get the absolute path of the project directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from model.data_loader import load_crude_runs, save_crude_runs
from model.crude_run import CrudeRunRecord
from view.display_view import display_records, display_statistics
from controller.statistics_controller import calculate_statistics
from controller.crude_run_controller import add_crude_run, update_crude_run, delete_crude_run  # Import the function

# Correct path to the CSV file inside the 'data' folder
file_path = os.path.join(BASE_DIR, "data", "crude-runs-weekly.csv")

# Load dataset
crude_run_records = load_crude_runs(file_path)

# Load dataset
crude_run_records = load_crude_runs(file_path)

def main():
    while True:
        print("\nMenu:")
        print("1. View records")
        print("2. Add record")
        print("3. Update record")
        print("4. Delete record")
        print("5. Save and Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            display_records(crude_run_records)
        elif choice == "2":
            date = input("Enter date (YYYY-MM-DD): ")
            crude_value = float(input("Enter crude volume: "))
            add_crude_run(crude_run_records, date, crude_value)
        elif choice == "3":
            date = input("Enter date to update: ")
            new_value = float(input("Enter new crude volume: "))
            update_crude_run(crude_run_records, date, new_value)
        elif choice == "4":
            date = input("Enter date to delete: ")
            crude_run_records = delete_crude_run(crude_run_records, date)
        elif choice == "5":
            save_crude_runs(file_path, crude_run_records)
            print("Changes saved. Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
