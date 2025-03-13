import csv
import uuid
import os
from collections import defaultdict

class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = []
        self.data_dict = defaultdict(list)

    def load_data(self):
        """Load data from a CSV file into a list and dictionary."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        date = row['Week End']
                        crude_runs = float(row['Crude Volumes For The Week'])
                        self.data.append([date, crude_runs])
                        self.data_dict[date].append(crude_runs)
                    except KeyError as e:
                        print(f"Skipping row due to missing key: {e}")
                    except ValueError as e:
                        print(f"Skipping row due to value error: {e}")
        except FileNotFoundError:
            print(f"Error: The file '{self.file_path}' was not found.")
        except Exception as e:
            print(f"Unexpected error: {e}")

    def get_data(self):
        """Returns the raw data."""
        return self.data

    def get_sorted_data(self, column_index):
        """Sort data based on the given column index using Merge Sort."""
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
                if left[i][column_index] < right[j][column_index]:
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
        """Retrieve records by key (Binary Search if sorted)."""
        return self.data_dict.get(key, [])

    def save_data(self):
        """Save crude run data to a new CSV file with a UUID-based name."""
        base_dir = os.path.dirname(os.path.abspath(self.file_path))
        data_dir = os.path.join(base_dir, "data")
        os.makedirs(data_dir, exist_ok=True)
        
        filename = f"crude-runs-{uuid.uuid4().hex[:8]}.csv"
        file_path = os.path.join(data_dir, filename)
        
        try:
            with open(file_path, mode="w", newline="", encoding='utf-8') as file:
                writer = csv.writer(file)
                writer.writerow(["Date", "Crude Volume"]) 
                writer.writerows(self.data)
            print(f"Data successfully saved to {file_path}")
        except Exception as e:
            print(f"Error saving data: {e}")

