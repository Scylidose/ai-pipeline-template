import csv
import os
from dotenv import load_dotenv

load_dotenv()

# Retrieve the path of the CSV file to read.
# csv_file_path = os.getenv("CSV_FILE_PATH")

def get_csv_file_content(csv_file_path):
    """
    Read data from a CSV file and return a list of rows.

    Args:
        csv_file (str): The path to the CSV file.

    Returns:
        list: A list of rows, where each row is represented as a list of values.
    """
    data = []

    with open(csv_file_path, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)

    return data
