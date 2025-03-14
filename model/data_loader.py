import csv
import os
import sys
import uuid
from collections import defaultdict
from model.crude_run import CrudeRunRecord

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []
        self.data_dict = defaultdict(list)

    def load_crude_runs(self):
        """Load data from a CSV file into a list of CrudeRunRecord objects."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        date = row['Week End']
                        crude_runs = float(row['Crude Volumes For The Week'])
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
        """Returns the list of CrudeRunRecord objects."""
        return self.data

    def search_by_key(self, key):
        """Retrieve records by key using Binary Search (list must be sorted)."""
        sorted_data = self.get_sorted_data("date")
        left, right = 0, len(sorted_data) - 1
        while left <= right:
            mid = (left + right) // 2
            if sorted_data[mid].date == key:
                return sorted_data[mid]
            elif sorted_data[mid].date < key:
                left = mid + 1
            else:
                right = mid - 1
        return None

    def get_sorted_data(self, key):
        """Sort data based on a given attribute using Merge Sort."""
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

    def save_data(self):
        """Save crude run data to a CSV file inside the data folder with a unique name."""
        base_dir = os.path.dirname(os.path.abspath(self.file_path))
        data_dir = os.path.join(base_dir, "data")
        os.makedirs(data_dir, exist_ok=True)
        random_filename = f"crude-runs-{uuid.uuid4().hex}.csv"
        file_path = os.path.join(data_dir, random_filename)

        try:
            with open(file_path, mode="w", newline="", encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Week End", "Crude Volumes For The Week"])
                for record in self.data:
                    writer.writerow([record.date, record.crude_runs])
            print(f"Data successfully saved to {file_path}")
        except Exception as e:
            print(f"Error saving data: {e}")

