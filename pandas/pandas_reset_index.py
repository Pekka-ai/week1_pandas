"""
We create a DataFrame (df) with some sample data.
We set the 'Name' column as the index of the DataFrame using set_index().
We display the DataFrame with the 'Name' column as the index.
We use the reset_index() function to reset the index and make the 'Name' column a regular column again.
We display the resulting DataFrame after using reset_index().
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

# Set the 'Name' column as the index
df.set_index('Name', inplace=True)

# Display the DataFrame with the 'Name' column as the index
print("DataFrame with 'Name' as Index:")
print(df)

# Use reset_index() to reset the index and make 'Name' a regular column
df_reset = df.reset_index()

# Display the DataFrame after using reset_index()
print("\nDataFrame after using reset_index():")
print(df_reset)
