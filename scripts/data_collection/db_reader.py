import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

# Retrieve the path of the CSV file to read.
# database_file_path = os.getenv("DB_FILE_PATH")
# table = os.getenv("DB_TABLE_NAME")

def get_data_from_table(database_file, table_name):
    """
    Connect to an SQLite database, execute a query to retrieve data from a table,
    and return the fetched data as a list of rows.

    Args:
        database_file (str): The path to the SQLite database file.
        table_name (str): The name of the table from which to retrieve data.

    Returns:
        list: A list of rows, where each row is represented as a tuple of values.
    """
    data = []

    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM {table_name}")
    data = cursor.fetchall()

    conn.close()

    return data
