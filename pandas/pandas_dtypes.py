"""
We create a DataFrame (df) with some sample data.
We display the original DataFrame.
We use the dtypes attribute to get the data types of each column in the DataFrame.
We display the data types of each column.
"""

import pandas as pd

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

# Use the dtypes attribute to get the data types of each column
column_data_types = df.dtypes

# Display the data types of each column
print("\nData Types of Each Column:")
print(column_data_types)