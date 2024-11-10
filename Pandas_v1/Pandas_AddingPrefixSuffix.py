# Example 34: Pandas - Adding a Prefix or Suffix to Column Names
import pandas as pd

# Creating a DataFrame
data = {'Math':[90, 80], 'Science':[85, 88]}

df = pd.DataFrame(data)# Adding a suffix to column names

# Adding a prefix to column names
df_prefix = df.add_prefix('Grade_')

# Adding a suffix to column names
df_suffix = df.add_suffix('_Score')

# Printing
print('Original Data:\n', df)
print('DataFrame with Prefix:\n', df_prefix)
print('DataFrame with Suffix:\n', df_suffix)