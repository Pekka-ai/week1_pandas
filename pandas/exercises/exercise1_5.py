import pandas as pd
import random


names = ['Seppo', 'Erkki', 'Mari', 'Emma', 'Taavi']

ages = [10, 32, 10, 32, 10]

scores = [83, 44, None, 42, None]

data = {
    'Name': names,
    'Age': ages,
    'Score': scores
}

df = pd.DataFrame(data)

df['Score'] = df['Score'].fillna(50)

#tulostetaan dataframe
print(df)
