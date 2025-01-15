import pandas as pd

file_path = 'titanic.csv'

df = pd.read_csv(file_path)

filtered_df = df.loc[(df['Siblings/Spouses Aboard']>0) | (df['Parents/Children Aboard']>0) ]
filtered_df = filtered_df[['Pclass', 'Name', 'Age']].reset_index()
filtered_df = filtered_df.rename(columns={'index': 'OldIndex'})

# filtered_df = (
#     df.loc[(df['Siblings/Spouses Aboard'] == 1) | (df['Parents/Children Aboard'] == 1), ['Pclass', 'Name', 'Age']]
#     .reset_index()
#     .rename(columns={'index': 'OldIndex'})
# )

print(filtered_df)

