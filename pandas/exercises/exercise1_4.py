import pandas as pd
import random


names = ['Seppo', 'Erkki', 'Mari', 'Emma', 'Taavi']

ages = [10, 32, 10, 32, 10]

scores = [random.randint(0, 100) for _ in range(5)]

data = {
    'Name': names,
    'Age': ages,
    'Score': scores
}

df = pd.DataFrame(data)

#tulostetaan dataframe
print(df)
grouped_df = df.groupby('Age')['Score'].mean()
print(grouped_df)