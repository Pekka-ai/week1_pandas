"""
We create a DataFrame (df) with sample data.
We display the original DataFrame.
We use the to_csv() function to write the DataFrame to a CSV file named 'example_output.csv'. The index=False parameter is used to exclude the DataFrame index from being written to the file.
We read the CSV file back into a new DataFrame (new_df) for verification.
We display the new DataFrame read from the CSV file.
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

# Save the DataFrame to a CSV file named 'example_output.csv'
df.to_csv('example_output.csv', index=False)

# Read the CSV file back into a new DataFrame for verification
new_df = pd.read_csv('example_output.csv')

# Display the new DataFrame
print("\nDataFrame read from CSV file:")
print(new_df)

