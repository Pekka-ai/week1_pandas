'''
The head() and tail() functions in Pandas are used to display the first and last
few rows of a DataFrame, respectively. These functions are helpful for quickly 
inspecting the structure and content of a DataFrame.
'''

import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace'],
    'Age': [25, 30, 22, 35, 28, 40, 32],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago', 'Miami', 'Seattle', 'Boston']
}

df = pd.DataFrame(data)

# Use the head() function to display the first few rows (default is 5 rows)
print("First 3 rows:")
print(df.head(3))  # Display the first 3 rows

# Use the tail() function to display the last few rows (default is 5 rows)
print("\nLast 2 rows:")
print(df.tail(2))  # Display the last 2 rows
