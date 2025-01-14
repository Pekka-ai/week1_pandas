'''
count: Number of non-null values in each column.
mean: Mean (average) of the values.
std: Standard deviation, a measure of the amount of variation or dispersion.
min: Minimum value in each column.
25%: First quartile (25th percentile).
50%: Median (50th percentile).
75%: Third quartile (75th percentile).
max: Maximum value in each column.
'''

# import pandas as pd
import pandas as pd

# Create a sample DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': [10.5, 20.3, 15.8, 25.1, 30.7],
    'C': ['apple', 'banana', 'orange', 'apple', 'orange']
}

df = pd.DataFrame(data)

# Use the describe function
description = df.describe()

# Display the result
print(description)

# Include non-numeric columns
description_all = df.describe(include='all')
print(description_all)

