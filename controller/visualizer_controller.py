import matplotlib.pyplot as plt

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

def visualize_crude_run_data(data_loader):
    """
    Visualizes crude run data using vertical bar charts.
    
    :param data_loader: The DataLoader instance containing the dataset.
    """
    # Get the necessary data for visualization
    data = data_loader.get_visualization_data()  # This method returns a list of dicts with 'date' and 'crude_runs'
    
    # Plot vertical bar chart for crude runs over time
    plot_vertical_bar_chart(data, 'date', 'crude_runs')
