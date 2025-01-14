import pandas as pd

file_path = 'titanic.csv'

df = pd.read_csv(file_path, usecols=['Name', 'Sex', 'Age', "Survived", "Fare"])
#df = pd.read_csv(file_path)


df.loc[df['Age']<18, 'Sex'] = 'Child'

female = df.loc[df['Sex']=='female']
male = df.loc[df['Sex']=='male']
child = df.loc[df['Sex']=='Child']
print(child)
print("--------------------")
print(female)
print("--------------------")
print(male)

