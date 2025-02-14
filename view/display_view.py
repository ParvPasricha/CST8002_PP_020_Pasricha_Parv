
from tabulate import tabulate


def display_records(records):
    """
    Displays a list of crude run records.
    """
    if not records:
        print("\nNo records available.")
        return
    print("\nLoaded Crude Run Records:")
    for record in records:
        print(record)

def display_statistics(avg_crude, max_crude, min_crude):
    """
    Displays crude run statistics.
    """
    if avg_crude is None:
        print("\nNo statistics available. Check data file.")
        return
    print("\nStatistics:")
    print(f"Average Crude Runs: {avg_crude:.2f} Thousand Cubic Meters per Day")
    print(f"Max Crude Runs: {max_crude:.2f} Thousand Cubic Meters per Day")
    print(f"Min Crude Runs: {min_crude:.2f} Thousand Cubic Meters per Day")


def display_records(records):
    """
    Displays a list of crude run records in a table format.
    """
    if not records:
        print("No records to display.")
        return

    table_data = [[record.date, f"{record.crude_runs:.2f}"] for record in records]
    headers = ["Date", "Crude Runs (Thousand Cubic Meters/Day)"]

    print("\nCrude Run Records:\n")
    print(tabulate(table_data, headers=headers, tablefmt="grid"))

def display_statistics(avg_crude, max_crude, min_crude):
    """
    Displays crude run statistics in a cleaner format.
    """
    print("\nCrude Run Statistics:\n")
    print(f"🟢 Average Crude Runs: {avg_crude:.2f} Thousand Cubic Meters/Day")
    print(f"🔵 Max Crude Runs: {max_crude:.2f} Thousand Cubic Meters/Day")
    print(f"🔴 Min Crude Runs: {min_crude:.2f} Thousand Cubic Meters/Day")
