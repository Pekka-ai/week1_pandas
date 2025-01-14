"""
We create a DataFrame (df) with some sample data.
We display the original DataFrame.
We use the shape attribute to get the dimensions of the DataFrame, which returns a tuple in the form (number_of_rows, number_of_columns).
We display the dimensions of the DataFrame.
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

# Use the shape attribute to get the dimensions of the DataFrame
df_shape = df.shape

# Display the dimensions of the DataFrame
print("\nDimensions of the DataFrame:")
print(df_shape)