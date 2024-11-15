# Example 31: Pandas - Using explode() for Nested JSON Columns
import pandas as pd

# Creating a DataFrame with nested lists
data = {'ID':[1, 2], 'Hobbies':[['Reading','Swimming','Gamming'], ['Hiking','Drawing']]}
df = pd.DataFrame(data)


# Exploding the 'Hobbies' column
exploded_df = df.explode('Hobbies')

print('Original DataFrame:\n', df)
print('DataFrame after Exploding Nested JSON Column:\n', exploded_df)
