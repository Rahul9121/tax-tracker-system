import sqlite3

# Connect to SQLite database (this will create a new database if it doesn't exist)
connection = sqlite3.connect('my_database.db')

# Create a cursor object to execute SQL queries
import sqlite3

# Connect to SQLite database (this will create a new database if it doesn't exist)
connection = sqlite3.connect('my_database.db')  # Replace 'your_database_name' with the desired name

# Create a cursor object to execute SQL queries
cursor = connection.cursor()

# Define the table schema
create_table_query = '''
CREATE TABLE IF NOT EXISTS my_table (
    id INTEGER PRIMARY KEY,
    category TEXT,
    amount REAL,
    date_paid TEXT,
    status TEXT,
    due_date TEXT
);
'''

# Execute the create table query
cursor.execute(create_table_query)

# Insert data into the table
data = [
    (1, 'derm', 4100.00, '2023-09-26', 'paid', '2024-01-15'),
    (2, 'derm', 4100.00, '2023-10-12', 'paid', '2024-01-15'),
    (3, 'tek', 15200.00, '2023-06-09', 'paid', '2023-06-15'),
    (4, 'tek', 15200.00, '2023-07-12', 'paid', '2023-09-15'),
    (5, 'tek', 11400.00, '2023-08-11', 'paid', '2023-09-15'),
    (6, 'tek', 14440.00, '2023-09-21', 'paid', '2024-01-15'),
    (7, 'tek', 15200.00, '2023-10-18', 'paid', '2024-01-15'),
    (8, 'tek', 23520.00, None, 'unpaid', '2024-01-15'),  # Use None for NULL
    (9, 'tek', 16800.00, None, 'unpaid', '2024-01-15'),
    (10, 'tek', 16800.00, None, 'unpaid', '2024-01-15'),
    (11, 'tek', 16800.00, None, 'unpaid', '2024-01-15')
]

# Insert data into the table
cursor.executemany('INSERT INTO my_table VALUES (?, ?, ?, ?, ?, ?)', data)

# Commit the changes and close the connection
connection.commit()
connection.close()



