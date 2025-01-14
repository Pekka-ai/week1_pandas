"""
We create a DataFrame (df) with some sample data.
We display the original DataFrame.
We define a custom function (add_prefix) that adds a prefix ("Mr. ") to each element in the 'Name' column.
We use the apply() function to apply the custom function to the 'Name' column, modifying its elements.
We display the resulting DataFrame after using apply().
"""

import pandas as pd

# Create a DataFrame with some sample data
data = {
    'Name': ['John', 'Alice', 'Bob', 'Emma'],
    'Age': [28, 35, 22, 40],
    'Occupation': ['Engineer', 'Data Scientist', 'Student', 'Manager']
}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Define a custom function to add a prefix to each element in the 'Name' column
def add_prefix(name):
    return f'Mr. {name}'

# Use apply() to apply the custom function to the 'Name' column
df['Name'] = df['Name'].apply(add_prefix)

# Display the DataFrame after using apply()
print("\nDataFrame after using apply():")
print(df)
