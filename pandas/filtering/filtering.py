import pandas as pd

# Assuming you have a CSV file named 'example_data.csv' in the same directory
file_path = 'filtering\dataset_for_filtering.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)
print(df)
print("--------------------")

# Basic filtering
filtered_df = df[df['Age'] > 30]
print(filtered_df)
print("--------------------")

# Multiple conditions
filtered_df = df[(df['Age'] > 30) & (df['Gender'] == 'Female')] 
print(filtered_df)
print("--------------------")

# is in -condition (values list is the condition here)
values = ['USA', 'Canada']
filtered_df = df[df['Country'].isin(values)]
print(filtered_df)
print("--------------------")

# Select only some columns after filtering
filtered_df = df.loc[df['Age'] > 30, ['Age', 'Name']] 
print(filtered_df)
print("--------------------")

# notna -condition
filtered_df = df[df['Country'].notna()] 
print(filtered_df)
