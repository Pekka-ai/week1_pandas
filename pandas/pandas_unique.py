"""
We create a DataFrame (df) with a 'Category' column containing some repeated values.
We display the original DataFrame.
We use the unique() function on the 'Category' column to get an array of unique values.
We display the unique values in the 'Category' column.
"""

import pandas as pd

# Create a DataFrame with some sample data
data = {
    'Category': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'B', 'C'],
    'Value': [10, 15, 20, 25, 30, 35, 40, 45, 50]
}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Use unique() to get unique values in the 'Category' column
unique_categories = df['Category'].unique()

# Display the unique values in the 'Category' column
print("\nUnique Values in the 'Category' Column:")
print(unique_categories)
