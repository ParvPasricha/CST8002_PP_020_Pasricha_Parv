
from tabulate import tabulate


def display_records(records):
    """Display crude run records with the name every 10 records."""
    if not records:
        print("No records to display.")
        return

    for i, record in enumerate(records, start=1):
        print(f"{record.date}: {record.volume}")
        if i % 10 == 0:  # Every 10 records
            print("\n--- Developed by: Parv Pasricha ---\n")


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
