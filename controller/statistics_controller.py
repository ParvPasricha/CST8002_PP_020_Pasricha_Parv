# controller/statistics_controller.py

def calculate_statistics(records):
    """
    Calculate statistics for crude run records.
    Returns the average, max, and min crude run values.
    """
    if not records:
        return None, None, None
    
    crude_values = [record.crude_runs for record in records]
    avg_crude = sum(crude_values) / len(crude_values)
    max_crude = max(crude_values)
    min_crude = min(crude_values)

    return avg_crude, max_crude, min_crude
