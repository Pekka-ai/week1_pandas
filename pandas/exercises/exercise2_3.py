import pandas as pd

# Assuming you have a CSV file named 'example_data.csv' in the same directory
file_path = 'titanic.csv'

# Read the CSV file into a pandas DataFrame
#df = pd.read_csv(file_path)
df_fil_col = pd.read_csv(file_path, usecols=['Name', 'Sex', 'Age'])

#df.loc[df['Age']<18, 'Sex'] = 'Child'
df_fil_col.loc[df_fil_col['Age']<18, 'Sex'] = 'Child'
print(df_fil_col)
