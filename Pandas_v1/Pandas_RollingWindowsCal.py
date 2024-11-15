# Example 11: Pandas - Rolling Window Calculations
import pandas as pd

# Creating a time series DataFrame

data_range = pd.date_range(start='2024-10-01', periods=10, freq='D')
data = {'Sales': [100, 200, 150, 300, 250, 400, 300, 350, 300, 400]}

df = pd.DataFrame(data, index=data_range)

# Calculating a rolling mean with a window of 3 days
df['Rolling Mean'] = df['Sales'].rolling(window=3).mean()

print('DataFrame with Rolling Mean:\n', df)