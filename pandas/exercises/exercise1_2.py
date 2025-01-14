import pandas as pd
import random

# List of names
names = ['Seppo', 'Erkki', 'Mari', 'Emma', 'Taavi']

# Generate random ages between 18 and 40
ages = [30, 40, 20, 32, 10]

# Generate random scores between 0 and 100
scores = [random.randint(0, 100) for _ in range(5)]

data = {
    'Name': names,
    'Age': ages,
    'Score': scores
}

df = pd.DataFrame(data)

#tulostetaan dataframe
print(df)
#indeksoidaan nimellä
dfindexed = df.set_index('Name')
#filteröidään iällä
dffiltered = dfindexed[(dfindexed['Age'] > 25)] 
print(dfindexed)
print(dffiltered)