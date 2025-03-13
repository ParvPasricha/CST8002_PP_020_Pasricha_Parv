import unittest
import os
import sys
# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from controller.crude_run_controller import add_crude_run
from model.crude_run import CrudeRunRecord

class TestCrudeRunController(unittest.TestCase):
    def test_add_crude_run(self):
        """Test if adding a record updates the data structure correctly."""
        crude_run_records = []  # Start with an empty list
        
        print("\n--- Developed by: Parv Pasricha ---\n")
        # Add a new record
        add_crude_run(crude_run_records, "2025-02-13", 5000.0)
        
        # Assertions
        self.assertEqual(len(crude_run_records), 1)  # List should now have 1 record
        self.assertEqual(crude_run_records[0].date, "2025-02-13")
        self.assertEqual(crude_run_records[0].crude_runs, 5000.0)

if __name__ == "__main__":
    unittest.main()
