""" 
We create a DataFrame (df) with sample data.
We display the original DataFrame.
We create a SQLite database connection using sqlite3.
We use the to_sql() function to write the DataFrame to a SQL table named 'people' in the SQLite database. The index=False parameter is used to exclude the DataFrame index from being written to the SQL table. The if_exists='replace' parameter specifies that if the table already exists, it should be replaced.
We read the SQL table back into a new DataFrame (new_df) for verification using pd.read_sql.
We display the new DataFrame read from the SQL table. 
"""
import pandas as pd
import sqlite3

# Create a DataFrame with some sample data
data = {
    'Name': ['John', 'Alice', 'Bob', 'Emma', 'David'],
    'Age': [28, 35, 22, 40, 31],
    'Location': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Boston'],
    'Occupation': ['Engineer', 'Data Scientist', 'Student', 'Marketing Manager', 'Software Developer']
}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Create a SQLite database connection
conn = sqlite3.connect('example.db')

# Save the DataFrame to a SQL table named 'people'
df.to_sql('people', con=conn, index=False, if_exists='replace')

# Read the SQL table back into a new DataFrame for verification
query = 'SELECT * FROM people'
new_df = pd.read_sql(query, con=conn)

# Display the new DataFrame
print("\nDataFrame read from SQL table:")
print(new_df)

# Close the database connection
conn.close()