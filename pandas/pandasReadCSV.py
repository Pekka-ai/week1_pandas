# Import pandas library as variable named pd
import pandas as pd

# Assuming you have a CSV file named 'example_data.csv' in the same directory
file_path = 'example_data.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print("First few rows of the DataFrame:")
print(df.head())

# Perform some basic analysis or manipulations
# For example, calculating the mean of a column
mean_value = df['Age'].mean()
print(f"\nMean value of 'Age': {mean_value}")