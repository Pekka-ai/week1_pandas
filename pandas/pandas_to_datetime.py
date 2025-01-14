"""
We create a DataFrame (df) with some sample data, including a 'Date' column with date strings.
We display the original DataFrame.
We use the to_datetime() function to convert the 'Date' column to datetime format.
We display the resulting DataFrame after using to_datetime().
"""

import pandas as pd

# Create a DataFrame with some sample data
data = {
    'Date': ['2022-01-15 08:30:00', '2022-02-20 12:45:00', '2022-03-25 16:00:00', '2022-04-30 20:15:00'],
    'Value': [10, 15, 20, 25]
}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Use to_datetime() to convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Display the DataFrame after using to_datetime()
print("\nDataFrame after using to_datetime():")
print(df)

