import pandas as pd

# Create a DataFrame with some sample data
data = {
    'Category': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'B', 'C'],
    'Value': [10, 15, 20, 25, 30, 35, 40, 45, 50]
}

df = pd.DataFrame(data)

# Display the original DataFrame
print("Original DataFrame:")
print(df)

# Use nunique() to count the number of unique values in the 'Category' column
num_unique_categories = df['Category'].nunique()

# Display the number of unique values in the 'Category' column
print("\nNumber of Unique Values in the 'Category' Column:")
print(num_unique_categories)