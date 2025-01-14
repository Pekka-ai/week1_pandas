"""
We create a DataFrame (df) with some missing values (represented by None).
We display the original DataFrame.
We use the fillna() function on the DataFrame to fill missing values with specified values. In this case, we fill the 'Name' column with 'Unknown', the 'Age' column with the mean age, and the 'Occupation' column with 'Unknown'.
We display the DataFrame after filling missing values.
"""

import pandas as pd

# Create a DataFrame with some missing values
data = {
    'Name': ['John', 'Alice', 'Bob', None, 'David'],
    'Age': [28, 35, None, 40, 31],
    'Location': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Boston'],
    'Occupation': ['Engineer', 'Data Scientist', 'Student', None, 'Software Developer']
}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Use fillna() to fill missing values with specified values
df_filled = df.fillna({'Name': 'Unknown', 'Age': df['Age'].mean(), 'Occupation': 'Unknown'})

# Display the DataFrame after filling missing values
print("\nDataFrame after Filling Missing Values:")
print(df_filled)