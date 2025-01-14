"""
We create a DataFrame (df) with some sample data.
We display the original DataFrame.
We use the replace() function to replace values in the 'Location' column. In this case, we replace 'New York' with 'NYC', 'Los Angeles' with 'LA', and 'Chicago' with 'CHI'.
We display the DataFrame after using replace().
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

# Use replace() to replace values in the 'Location' column
df.replace({'Location': {'New York': 'NYC', 'Los Angeles': 'LA', 'Chicago': 'CHI'}}, inplace=True)

# Display the DataFrame after using replace()
print("\nDataFrame after using replace():")
print(df)
