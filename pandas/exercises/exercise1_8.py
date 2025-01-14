import pandas as pd

# List of names
names = ['Seppo', 'Erkki', 'Mari', 'Emma', 'Taavi']
dates = ['2022-12-02', '2021-11-01', '2000-10-12', '2001-12-04', '1999-11-11']


data = {
    'Name': names,
    'Date': dates
}

# Create the DataFrame
df_1 = pd.DataFrame(data)
print (df_1)
df_1['Date'] = pd.to_datetime(df_1['Date'])

print(df_1)

