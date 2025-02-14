import os
import sys

# Add the project root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from model.crude_run import CrudeRunRecord

def add_crude_run(records, date, crude_value):
    new_record = CrudeRunRecord(date, crude_value)
    records.append(new_record)
    print(f"Added new record: {new_record}")

def update_crude_run(records, date, new_value):
    for record in records:
        if record.date == date:
            record.crude_runs = new_value
            print(f"Updated record: {record}")
            return
    print(f"No record found for date {date}.")

def delete_crude_run(records, date):
    updated_records = [record for record in records if record.date != date]
    if len(updated_records) < len(records):
        print(f"Deleted record with date: {date}")
    else:
        print(f"No record found for date {date}.")
    return updated_records
