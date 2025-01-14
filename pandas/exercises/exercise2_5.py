import pandas as pd

file_path = 'titanic.csv'

df = pd.read_csv(file_path, usecols=['Name', 'Sex', 'Age', "Survived", "Fare", "Pclass"])
#df = pd.read_csv(file_path)
average_fare_per_sex_pclass = df.groupby(['Sex', 'Pclass'])[['Fare', 'Survived']].mean().reset_index()

print(average_fare_per_sex_pclass)
print("--------------------")

