import pandas as pd

# Assuming you have a CSV file named 'example_data.csv' in the same directory
file_path = 'titanic.csv'

# Read the CSV file into a pandas DataFrame
df = pd.read_csv(file_path)
df.columns = df.columns.str.replace(r'[^A-Za-z0-9]', '', regex=True)

print(df)
print("--------------------")