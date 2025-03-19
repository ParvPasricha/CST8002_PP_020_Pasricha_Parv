import pytest
import os
import sys
import csv
import unittest
import shutil  # Required for recursive directory deletion

# Ensure the module can be imported even when running tests from a different directory
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from model.crude_run import CrudeRunRecord
from model.data_loader import DataLoader

class TestDataLoader(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up a dedicated test directory and create a test CSV file."""
        cls.test_dir = "test_output"  # Store all test-related files in this directory
        os.makedirs(cls.test_dir, exist_ok=True)  # Create the directory if it doesn't exist

        cls.test_file = os.path.join(cls.test_dir, "temp_test_crude_runs.csv")  # Define test file path

        # Create a CSV file with sample data for testing
        with open(cls.test_file, mode="w", newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Week End", "Crude Volumes For The Week"])
            writer.writerow(["03/01/2025", "5000"])  # Valid data
            writer.writerow(["03/08/2025", "6000"])  # Valid data
            writer.writerow(["03/15/2025", "-200"])  # Invalid: negative volume
            writer.writerow(["INVALID_DATE", "4000"])  # Invalid: incorrect date format

    @classmethod
    def setUp(self):
        """Initialize DataLoader with the test file for each test case."""
        self.loader = DataLoader(self.test_file)  # Load the test dataset

    def test_load_crude_runs(self):
        """Verify that only valid records are loaded from the test file."""
        self.loader.load_crude_runs()
        self.assertGreater(len(self.loader.get_data()), 0, "Data should not be empty after loading.")  # Ensure data is loaded
        self.assertEqual(len(self.loader.get_data()), 2, "Only valid records should be loaded.")  # Expect only two valid rows

    def test_sorting(self):
        """Ensure that sorting works correctly using the date field."""
        self.loader.load_crude_runs()
        sorted_data = self.loader.get_sorted_data("date")

        # Verify sorting order
        self.assertTrue(
            all(sorted_data[i].date <= sorted_data[i + 1].date for i in range(len(sorted_data) - 1)),
            "Data should be sorted by date."
        )

    def test_search_by_key(self):
        """Confirm that searching for an existing date returns the correct record."""
        self.loader.load_crude_runs()
        result = self.loader.search_by_key("03/01/2025")
        self.assertIsNotNone(result, "Search should return results for valid dates.")  # Ensure result exists
        self.assertEqual(len(result), 1, "Search should return exactly one record.")  # Expect exactly one match

    def test_save_data_csv(self):
        """Ensure that saving data in CSV format works within the test directory."""
        self.loader.load_crude_runs()
        test_save_path = os.path.join(self.test_dir, "crude-runs-weekly.csv")  # Define test save path

        self.loader.save_data(format='csv', file_path=test_save_path)  # Pass file path explicitly

        self.assertTrue(os.path.exists(test_save_path), f"CSV file should be created at {test_save_path}.")
        # Verify the file was created and then clean it up
        self.assertTrue(os.path.exists(test_save_path), "CSV file should be created.")
        os.remove(test_save_path)  # Remove test-generated file after verification



    def test_save_data_json(self):
        """Ensure that saving data in JSON format works within the test directory."""
        self.loader.load_crude_runs()
        test_save_path = os.path.join(self.test_dir, "crude-runs-weekly.json")  # Define test save path

        self.loader.save_data(format='json', file_path=test_save_path)  # Pass file path explicitly

        self.assertTrue(os.path.exists(test_save_path), f"JSON file should be created at {test_save_path}.")
        # Verify the file was created and then clean it up
        self.assertTrue(os.path.exists(test_save_path), "JSON file should be created.")
        os.remove(test_save_path)  # Remove test-generated file after verification


if __name__ == '__main__':
    unittest.main()
