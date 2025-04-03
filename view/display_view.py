
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

def plot_vertical_bar_chart(data, x_column, y_column):
    """
    Plots a vertical bar chart using the specified columns from the dataset.
    
    :param data: The dataset (list of dictionaries or Pandas DataFrame).
    :param x_column: The column to use for x-axis labels.
    :param y_column: The column to use for y-axis values.
    """
    # Extract values for plotting
    x_values = [row[x_column] for row in data]
    y_values = [row[y_column] for row in data]
    
    # Plotting the bar chart
    plt.figure(figsize=(10, 5))
    plt.bar(x_values, y_values, color='skyblue')
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.title(f'Vertical Bar Chart: {x_column} vs {y_column}')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Show the chart
    plt.show()