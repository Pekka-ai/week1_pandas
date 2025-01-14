"""
We create a DataFrame (df) with some sample data.
We display the original DataFrame.
We use the iterrows() function to iterate over the DataFrame rows and print the information for each row.
"""

import pandas as pd

# Create a DataFrame with some sample data
data = {
    'Name': ['John', 'Alice', 'Bob', 'Emma'],
    'Age': [28, 35, 22, 40],
    'Occupation': ['Engineer', 'Data Scientist', 'Student', 'Manager']
}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Use iterrows() to iterate over DataFrame rows
print("\nIterating over rows using iterrows():")
for index, row in df.iterrows():
    print(f"Index: {index}, Name: {row['Name']}, Age: {row['Age']}, Occupation: {row['Occupation']}")
