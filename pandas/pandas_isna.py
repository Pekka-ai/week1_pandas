"""
We create a DataFrame (df) with some missing values (represented by None).
We display the original DataFrame.
We use the isna() function on the DataFrame to create a boolean DataFrame where True indicates missing values and False indicates non-missing values.
We display the boolean DataFrame indicating missing values.
We use the sum() function to count the number of missing values in each column.
We display the count of missing values in each column.    
"""

import pandas as pd

# Create a DataFrame with some missing values
data = {
    'Name': ['John', 'Alice', 'Bob', None, 'David'],
    'Age': [28, 35, 22, None, 31],
    'Location': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Boston'],
    'Occupation': ['Engineer', 'Data Scientist', None, 'Marketing Manager', 'Software Developer']
}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Use isna() to check for missing values
missing_values = df.isna()

# Display the DataFrame indicating True for missing values and False otherwise
print("\nDataFrame with Missing Value Indicators:")
print(missing_values)

# Count the number of missing values in each column
missing_count = df.isna().sum()

# Display the count of missing values
print("\nCount of Missing Values in Each Column:")
print(missing_count)
