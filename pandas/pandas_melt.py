"""
We create a DataFrame (df_wide) with some sample data in wide format, where subjects and their scores are in separate columns.
We display the original DataFrame in wide format.
We use the melt() function to reshape the DataFrame to long format, where the subjects and scores are represented as rows instead of columns.
We display the DataFrame after using melt() in long format.
"""

import pandas as pd

# Create a DataFrame with some sample data in wide format
data = {
    'Name': ['John', 'Alice', 'Bob'],
    'Math_Score': [90, 85, 78],
    'English_Score': [88, 92, 85],
    'History_Score': [75, 80, 88]
}

df_wide = pd.DataFrame(data)

# Display the original DataFrame in wide format
print("Original DataFrame (Wide Format):")
print(df_wide)

# Use melt() to reshape the DataFrame to long format
df_long = pd.melt(df_wide, id_vars=['Name'], var_name='Subject', value_name='Score')

# Display the DataFrame after using melt() in long format
print("\nDataFrame after using melt() (Long Format):")
print(df_long)
