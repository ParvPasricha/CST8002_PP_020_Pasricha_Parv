import os
import sys

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from model.data_loader import DataLoader
from model.crude_run import CrudeRunRecord
from view.display_view import display_records, display_statistics
from controller.statistics_controller import calculate_statistics
from controller.visualizer_controller import visualize_crude_run_data
from controller.crude_run_controller import add_crude_run, update_crude_run, delete_crude_run

# Correct path to the CSV file inside the 'data' folder
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
data_dir = os.path.join(BASE_DIR, "data")
os.makedirs(data_dir, exist_ok=True)  # Ensure data directory exists
file_path = os.path.join(data_dir, "crude-runs-weekly.csv")

data_loader = DataLoader(file_path)
data_loader.load_crude_runs()
crude_run_records = data_loader.get_data()

def main():
    global crude_run_records  # Ensure we modify the global list
    
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
        print("6. View statistics")
        print("7. Reload dataset")
        print("8. View sorted data")
        print("9. Visualize crude run data (Bar chart)")
        print("10. Save and Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            if crude_run_records:
                try:
                    num_records = int(input("Enter number of records to view: "))
                    print("\nLoaded Crude Run Records:\n")
                    display_records(crude_run_records[:num_records])
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        
        elif choice == "2":
            date = input("Enter date (MM/DD/YYYY) to view record: ")
            record_found = data_loader.search_by_key(date)
            if record_found:
                print("\nRecord found:")
                print(record_found)
            
        
        elif choice == "3":
            date = input("Enter date (YYYY-MM-DD): ")
            try:
                crude_value = float(input("Enter crude volume: "))
                add_crude_run(crude_run_records, date, crude_value)
                print("Record added successfully.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        
        elif choice == "4":
            date = input("Enter date (MM/DD/YYYY) to update: ")
            try:
                new_value = float(input("Enter new crude volume: "))
                update_crude_run(crude_run_records, date, new_value)
                print("Record updated successfully.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == "5":
            date = input("Enter date (MM/DD/YYYY) to delete: ")
            crude_run_records = delete_crude_run(crude_run_records, date)
            print("Record deleted successfully.")
        
        elif choice == "6":
            avg_crude, max_crude, min_crude = calculate_statistics(crude_run_records)
            display_statistics(avg_crude, max_crude, min_crude)
        
        elif choice == "7":
            try:
                data_loader.load_crude_runs()
                crude_run_records = data_loader.get_data()
                print("Dataset reloaded successfully.")
            except FileNotFoundError:
                print("Error: Dataset not found.")
        
        elif choice == "8":
            sorted_records = data_loader.get_sorted_data("date")
            display_records(sorted_records)
        
        elif choice == "9":
            # Get start and end date from the user
            start_date = input("Enter start date (MM/DD/YYYY): ")
            end_date = input("Enter end date (MM/DD/YYYY): ")

            try:
                # Call visualize function with date range
                visualize_crude_run_data(data_loader, start_date, end_date)
            except ValueError:
                print("Invalid date format. Please use MM/DD/YYYY.")

        elif choice == "10":
            try:
                data_loader.save_data()
                print("Data saved successfully. Exiting...")
                break
            except Exception as e:
                print(f"Error saving data: {e}")
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
