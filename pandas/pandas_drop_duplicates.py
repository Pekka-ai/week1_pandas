"""
We create a DataFrame (df) with some sample data, including duplicate rows.
We display the original DataFrame.
We use the drop_duplicates() function to remove duplicate rows based on all columns.
We display the DataFrame after removing duplicate rows.
"""

import pandas as pd

# Create a DataFrame with some sample data including duplicate rows
data = {
    'Name': ['John', 'Alice', 'Bob', 'Alice', 'David', 'Bob'],
    'Age': [28, 35, 22, 35, 31, 22],
    'Location': ['New York', 'San Francisco', 'Los Angeles', 'San Francisco', 'Boston', 'Los Angeles'],
    'Occupation': ['Engineer', 'Data Scientist', 'Student', 'Data Scientist', 'Software Developer', 'Student']
}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Use drop_duplicates() to remove duplicate rows based on all columns
df_no_duplicates = df.drop_duplicates()

# Display the DataFrame after removing duplicate rows
print("\nDataFrame after using drop_duplicates():")
print(df_no_duplicates)
