import pandas as pd
import random

# List of names
names = ['Seppo', 'Erkki', 'Mari', 'Emma', 'Taavi']
# Generate random ages between 18 and 40
ages = [40, 50, 44, 20, 33]
# Generate random scores between 0 and 100
ids = [1, 2, 3, 4, 5]

ids_2 = [1, 2, 3, 4, 5]
# Generate random ages between 18 and 40
occupation = ["A", "B", "C", "D", "E"]
# Generate random scores between 0 and 100
salaries = [100, 33, 45, 53, 33]


data = {
    'Name': names,
    'Age': ages,
    'Id': ids
}


data_2 = {
    'Id': ids_2,
    'Occupation': occupation,
    'Salary': salaries
}

# Create the DataFrame
df_1 = pd.DataFrame(data)
df_2 = pd.DataFrame(data_2)
merged_df = pd.merge(df_1, df_2, on = 'Id', how = 'inner')


print(df_1)
print("*****************************")
print(df_2)
print("*****************************")
print(merged_df)
