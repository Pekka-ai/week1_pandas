import pandas as pd
import random

# List of names
names = ['Seppo', 'Erkki', 'Mari', 'Emma', 'Taavi']

# Generate random ages between 18 and 40
ages = [random.randint(18, 40) for _ in range(5)]

# Generate random scores between 0 and 100
scores = [random.randint(0, 100) for _ in range(5)]

data = {
    'Name': names,
    'Age': ages,
    'Score': scores
}

# Create the DataFrame
df = pd.DataFrame(data)

df['Score'] = df['Score'].astype(float)

# Display the DataFrame
print(df)
