"""
We create a DataFrame (df) with some sample data.
We display the original DataFrame.
We use the drop() function to remove a specific row (index 2) and a specific column ('Location'). Note that the drop() function returns a new DataFrame, and the original DataFrame remains unchanged unless you use the inplace=True parameter.
We display the modified DataFrame after using drop()
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

# Use drop() to remove a specific row (index 2) and a specific column ('Location')
df_modified = df.drop(index=2, columns='Location')

# Display the modified DataFrame
print("\nDataFrame after using drop():")
print(df_modified)
