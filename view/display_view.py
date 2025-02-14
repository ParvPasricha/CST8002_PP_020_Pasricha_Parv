# view/display_view.py

def display_records(records):
    """
    Displays a list of crude run records.
    """
    for record in records:
        print(record)

def display_statistics(avg_crude, max_crude, min_crude):
    """
    Displays crude run statistics.
    """
    print("\nStatistics:")
    print(f"Average Crude Runs: {avg_crude:.2f} Thousand Cubic Meters per Day")
    print(f"Max Crude Runs: {max_crude:.2f} Thousand Cubic Meters per Day")
    print(f"Min Crude Runs: {min_crude:.2f} Thousand Cubic Meters per Day")
