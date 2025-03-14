import csv
import os
import uuid
import sys
from collections import defaultdict
from datetime import datetime
from model.crude_run import CrudeRunRecord

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []
        self.data_dict = defaultdict(list)

    def load_crude_runs(self):
        """
        Reads a CSV file and initializes CrudeRunRecord objects with validation.
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        date = row['Week End']
                        crude_runs = float(row['Crude Volumes For The Week'])

                        # Validate date format (MM/DD/YYYY)
                        try:
                            datetime.strptime(date, "%m/%d/%Y")
                        except ValueError:
                            print(f"Skipping row due to invalid date format: {date}")
                            continue

                        # Validate crude volume
                        if crude_runs < 0:
                            print(f"Skipping row due to negative crude volume: {crude_runs}")
                            continue

                        record = CrudeRunRecord(date, crude_runs)
                        self.data.append(record)
                        self.data_dict[date].append(record)
                    except KeyError as e:
                        print(f"Skipping row due to missing key: {e}")
                    except ValueError as e:
                        print(f"Skipping row due to value error: {e}")
        except FileNotFoundError:
            print(f"Error: The file '{self.file_path}' was not found.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def get_data(self):
        """Returns the loaded data."""
        return self.data

    def get_sorted_data(self, key):
        """Sorts data based on the given key using Merge Sort."""
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left_half = merge_sort(arr[:mid])
            right_half = merge_sort(arr[mid:])
            return merge(left_half, right_half)
        
        def merge(left, right):
            sorted_list = []
            i = j = 0
            while i < len(left) and j < len(right):
                if getattr(left[i], key) < getattr(right[j], key):
                    sorted_list.append(left[i])
                    i += 1
                else:
                    sorted_list.append(right[j])
                    j += 1
            sorted_list.extend(left[i:])
            sorted_list.extend(right[j:])
            return sorted_list
        
        return merge_sort(self.data)

    def search_by_key(self, key):
        """Retrieve all records by key with validation and format the output."""
        if not key:
            print("Error: Search key cannot be empty.")
            return None

        try:
            search_date = datetime.strptime(key, "%m/%d/%Y").strftime("%m/%d/%Y")
        except ValueError:
            print("Error: Invalid date format. Use MM/DD/YYYY.")
            return None

        sorted_data = self.get_sorted_data("date")
        results = [record for record in sorted_data if record.date == search_date]

        if results:
            print("\nMatching Records:")
            for record in results:
                print(f"Date: {record.date}, Crude Volume: {record.crude_runs}")
        else:
            print("No records found for the given date.")



    def save_data(self):
        """Save crude run data to a CSV file inside the data folder."""
        base_dir = os.path.dirname(os.path.abspath(self.file_path))
        data_dir = os.path.join(base_dir, "data")
        os.makedirs(data_dir, exist_ok=True)
        file_path = os.path.join(data_dir, "crude-runs-weekly.csv")

        try:
            with open(file_path, mode="w", newline="", encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Week End", "Crude Volumes For The Week"])
                for record in self.data:
                    writer.writerow([record.date, record.crude_runs])
            print(f"Data successfully saved to {file_path}")
        except Exception as e:
            print(f"Error saving data: {e}")
