import pandas as pd

# List of names
names = ['Seppo', 'Seppo', 'Mari', 'Mari', 'Taavi']
dates = ['2022-12-02', '2021-11-01', '2000-10-12', '2001-12-04', '1999-11-11']
salaries = [100, 33, 45, 53, 33]


data = {
    'Name': names,
    'Date': dates,
    'Salary': salaries
}

# Create the DataFrame
df_1 = pd.DataFrame(data)
#print (df_1)
df_1['Date'] = pd.to_datetime(df_1['Date'])
unique_names = df_1['Name'].unique()

print(df_1)
print(unique_names)
