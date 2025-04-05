import csv
import json
import os
import uuid
import sys
import threading
from collections import defaultdict
from datetime import datetime
from model.crude_run import CrudeRunRecord

class DataLoader:

    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []
        self.data_dict = defaultdict(list)
        self.lock = threading.Lock()  # Ensures thread-safe operations

    def process_row(self, row):
        """Processes a single row and adds it to the dataset."""
        try:
            date = row['Week End']
            crude_runs = float(row['Crude Volumes For The Week'])

            # Validate date format (MM/DD/YYYY)
            datetime.strptime(date, "%m/%d/%Y")

            # Validate crude volume
            if crude_runs < 0:
                return

            record = CrudeRunRecord(date, crude_runs)

            # Use lock to ensure safe access to shared data
            with self.lock:
                self.data.append(record)
                self.data_dict[date].append(record)

        except (KeyError, ValueError):
            pass  # Skip invalid rows

    def load_crude_runs(self):
        """Loads data using multithreading."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                threads = []

                for row in reader:
                    thread = threading.Thread(target=self.process_row, args=(row,))
                    threads.append(thread)
                    thread.start()

                # Wait for all threads to complete
                for thread in threads:
                    thread.join()

        except FileNotFoundError:
            print(f"Error: The file '{self.file_path}' was not found.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def get_data(self):
        """Returns the loaded data."""
        return self.data


    def get_sorted_data(self, key):
        """Sorts data based on the given key using multithreaded Merge Sort."""
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            left_thread = threading.Thread(target=lambda: merge_sort(left_half))
            right_thread = threading.Thread(target=lambda: merge_sort(right_half))
            
            left_thread.start()
            right_thread.start()
            left_thread.join()
            right_thread.join()

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
        """Retrieve all records by key with validation."""
        if not key:
            print("Error: Search key cannot be empty.")
            return None
        
        try:
            search_date = datetime.strptime(key, "%m/%d/%Y").strftime("%m/%d/%Y")
        except ValueError:
            print("Error: Invalid date format. Use MM/DD/YYYY.")
            return None
        
        results = self.data_dict.get(search_date, [])
        
        if results:
            print("\nRecords found:")
            for record in results:
                print(f"Date: {record.date}, Crude Volume: {record.crude_runs}")
        else:
            print("No records found for the given date.")
        
        return results if results else None
    

    def get_visualization_data(self):
    # This method should now return the list of crude run records from 'self.data'
        return [{"date": record.date, "crude_runs": record.crude_runs} for record in self.data]


    def filter_records(self, date_filter=None, min_crude=None, max_crude=None):
        """Filter records by date and crude volume range."""
        filtered = self.data

        if date_filter:
            filtered = [r for r in filtered if r.date == date_filter]

        if min_crude is not None:
            try:
                min_val = float(min_crude)
                filtered = [r for r in filtered if r.crude_runs >= min_val]
            except ValueError:
                pass

        if max_crude is not None:
            try:
                max_val = float(max_crude)
                filtered = [r for r in filtered if r.crude_runs <= max_val]
            except ValueError:
                pass

        return filtered

    def sort_records(self, *keys):
        """Sorts data based on multiple columns (keys)."""
        def sort_key(record):
            return tuple(getattr(record, key) for key in keys)

        return sorted(self.data, key=sort_key)


    def save_data(self, format='csv', file_path=None):
        """Save crude run data to a specified file in CSV or JSON format."""
    
        # Use the provided file path; otherwise, save inside the 'data' folder
        if file_path is None:
            base_dir = os.path.dirname(os.path.abspath(self.file_path))
            data_dir = os.path.join(base_dir, "data")
            os.makedirs(data_dir, exist_ok=True)
            file_path = os.path.join(data_dir, f"crude-runs-weekly.{format}")

        try:
            if format == 'csv':
                with open(file_path, mode="w", newline="", encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow(["Week End", "Crude Volumes For The Week"])
                    for record in self.data:
                        writer.writerow([record.date, record.crude_runs])

            elif format == 'json':
                with open(file_path, mode="w", encoding='utf-8') as file:
                    json.dump([{ "Week End": record.date, "Crude Volumes For The Week": record.crude_runs } for record in self.data], file, indent=4)

            print(f"Data successfully saved to {file_path}")

        except Exception as e:
            print(f"Error saving data: {e}")