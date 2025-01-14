import pandas as pd

# Create a DataFrame with some sample data
data = {
    'Name': ['John', 'Alice', 'Bob', 'Emma', 'David'],
    'Age': [28, 35, 22, 40, 31],
    'Height': [5.8, 5.5, 6.0, 5.9, 6.2],
    'Occupation': ['Engineer', 'Data Scientist', 'Student', 'Marketing Manager', 'Software Developer']
}

df = pd.DataFrame(data)

# Display the original DataFrame with data types
print("Original DataFrame:")
print(df)
print("\nData Types of Each Column:")
print(df.dtypes)

# Use astype() to convert the 'Age' column from int to float
df['Age'] = df['Age'].astype(float)

# Use astype() to convert the 'Height' column from float to int (after rounding)
df['Height'] = df['Height'].astype(int)

# Display the DataFrame after using astype() for type conversion
print("\nDataFrame after using astype() for type conversion:")
print(df)
print("\nData Types of Each Column after astype() conversion:")
print(df.dtypes)
