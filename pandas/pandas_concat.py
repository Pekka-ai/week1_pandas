"""
We create two DataFrames (df1 and df2) with some sample data.
We display the original DataFrames.
We use the concat() function to concatenate the DataFrames along rows (axis=0). The ignore_index=True parameter is used to reindex the resulting DataFrame.
We display the resulting DataFrame after using concat().
"""

import pandas as pd

# Create two DataFrames with some sample data
data1 = {
    'ID': [1, 2, 3, 4],
    'Name': ['John', 'Alice', 'Bob', 'Emma'],
    'Age': [28, 35, 22, 40]
}

data2 = {
    'ID': [5, 6, 7, 8],
    'Name': ['Mike', 'Eva', 'Charlie', 'Sophie'],
    'Age': [45, 30, 28, 35]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Display the original DataFrames
print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)

# Use concat() to concatenate DataFrames along rows (axis=0)
concatenated_df = pd.concat([df1, df2], ignore_index=True)

# Display the DataFrame after using concat()
print("\nDataFrame after using concat():")
print(concatenated_df)
