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
