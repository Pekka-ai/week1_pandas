"""
We create two DataFrames (df1 and df2) with some sample data, both containing the 'ID' column.
We display the original DataFrames.
We use the merge() function to combine the DataFrames based on the common 'ID' column. The on parameter specifies the column to merge on, and the how parameter specifies the type of merge (in this case, an inner merge).
We display the resulting DataFrame after using merge().
"""

import pandas as pd

# Create two DataFrames with some sample data
data1 = {
    'ID': [1, 2, 3, 4],
    'Name': ['John', 'Alice', 'Bob', 'Emma'],
    'Age': [28, 35, 22, 40]
}

data2 = {
    'ID': [2, 3, 4, 5],
    'Occupation': ['Engineer', 'Data Scientist', 'Student', 'Manager'],
    'Salary': [90000, 120000, 25000, 80000]
}

df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

# Display the original DataFrames
print("DataFrame 1:")
print(df1)
print("\nDataFrame 2:")
print(df2)

# Use merge() to combine DataFrames based on the 'ID' column
merged_df = pd.merge(df1, df2, on='ID', how='inner')

# Display the DataFrame after using merge()
print("\nDataFrame after using merge():")
print(merged_df)
