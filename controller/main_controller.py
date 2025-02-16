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

def main():
    global crude_run_records  # Ensure we modify the global list

    print(type(crude_run_records[0]))


    while True:
        print("\n====================================")
        print("Crude Run Management System")
        print("Developed by: Parv Pasricha")
        print("====================================")
        
        print("\nMenu:")
        print("1. View first N records")
        print("2. View record by date")
        print("3. Add record")
        print("4. Update record")
        print("5. Delete record")
        print("6. View Statistics")
        print("7. Reload Dataset")
        print("8. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            if crude_run_records:
                try:
                    num_records = int(input("Enter number of records to view: "))
                    print("\nLoaded Crude Run Records:\n")
                    display_records(crude_run_records[:num_records])  # Show user-defined number of records
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
            else:
                print("No records available.")
        
        elif choice == "2":
            date = input("Enter date (YYYY-MM-DD) to view record: ")
            record_found = next((record for record in crude_run_records if record.date == date), None)
            if record_found:
                print("\nRecord found:")
                print(record_found)
            else:
                print("No record found for the given date.")
        
        elif choice == "3":
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                crude_value = float(input("Enter crude volume: "))
                add_crude_run(crude_run_records, date, crude_value)
                print("Record added successfully.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        elif choice == "4":
            date = input("Enter date to update: ")
            try:
                new_value = float(input("Enter new crude volume: "))
                update_crude_run(crude_run_records, date, new_value)
                print("Record updated successfully.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == "5":
            date = input("Enter date to delete: ")
            crude_run_records = delete_crude_run(crude_run_records, date)
            print("Record deleted successfully.")

        elif choice == "6":
            avg_crude, max_crude, min_crude = calculate_statistics(crude_run_records)
            display_statistics(avg_crude, max_crude, min_crude)
        
        elif choice == "7":
            try:
                crude_run_records = load_crude_runs(file_path)[:100]  # Reload up to 100 records
                print("Dataset reloaded successfully.")
            except FileNotFoundError:
                print("Error: Dataset file not found.")

        elif choice == "8":
            save_crude_runs(crude_run_records)
            print("Changes saved. Exiting...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
