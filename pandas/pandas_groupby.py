"""
We create a DataFrame (df) with some sample data containing a 'Category' column and a 'Value' column.
We display the original DataFrame.
We use the groupby() function to group the DataFrame by the 'Category' column.
We apply the mean() function to calculate the mean for each group.
We display the resulting DataFrame after using groupby() and mean().
"""

import pandas as pd

# Create a DataFrame with some sample data
data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'A', 'B', 'B'],
    'Value': [10, 15, 20, 25, 30, 35, 40, 45]
}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Use groupby() to group the DataFrame by 'Category' and calculate the mean for each group
grouped_df = df.groupby('Category').mean()

# Display the DataFrame after using groupby() and mean()
print("\nDataFrame after using groupby() and mean():")
print(grouped_df)
