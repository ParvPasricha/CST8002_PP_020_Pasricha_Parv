# model/crude_run.py

class CrudeRunRecord:
    """
    Represents a single record of crude runs data.
    
    Attributes:
        date (str): The date of the record.
        crude_runs (float): Crude runs in thousand cubic meters per day.
    """

    def __init__(self, date: str, crude_runs: float):
        self.date = date
        self.crude_runs = crude_runs

    def __str__(self):
        return f"Date: {self.date}, Crude Runs: {self.crude_runs:.2f} Thousand Cubic Meters per Day"
