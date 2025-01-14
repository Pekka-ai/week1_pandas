import pandas as pd

file_path = 'titanic.csv'

df = pd.read_csv(file_path, usecols=['Name', 'Sex', 'Age', "Survived", "Fare"])
#df = pd.read_csv(file_path)
grouped_df = df.groupby('Survived')['Fare'].mean().reset_index()


print(grouped_df)
print("--------------------")


