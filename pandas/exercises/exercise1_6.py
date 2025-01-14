import pandas as pd
import random

# List of names
names = ['Seppo', 'Erkki', 'Mari', 'Emma', 'Taavi']
# Generate random ages between 18 and 40
ages = [40, 50, 44, 20, 33]
# Generate random scores between 0 and 100
scores = [99, 39, 44, 55, 66]

names_2 = ['Ville', 'Jukka', 'Pekka', 'Maria', 'Iida']
# Generate random ages between 18 and 40
ages_2 = [14, 53, 22, 34, 39]
# Generate random scores between 0 and 100
scores_2 = [100, 33, 45, 53, 33]


data = {
    'Name': names,
    'Age': ages,
    'Score': scores
}


data_2 = {
    'Name': names_2,
    'Age': ages_2,
    'Score': scores_2
}

# Create the DataFrame
df_1 = pd.DataFrame(data)
df_2 = pd.DataFrame(data_2)

concatenated_df = pd.concat([df_1, df_2], ignore_index=True)

print(df_1)
print("*****************************")
print(df_2)
print("*****************************")
print(concatenated_df)
