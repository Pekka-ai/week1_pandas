"""
We create a DataFrame (df) with some sample data.
We display the original DataFrame.
We use the set_index() function to set the 'Name' column as the index of the DataFrame.
We display the resulting DataFrame after using set_index().
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

# Use set_index() to set the 'Name' column as the index
df_indexed = df.set_index('Name')

# Display the DataFrame after using set_index()
print("\nDataFrame after using set_index():")
print(df_indexed)
