# Example 10: Pandas - Creating Custom Categorical Data
import pandas as pd

# Creating a DataFrame

data = {'Name':['Alice','Bob', 'Charlie','David'], 'Score':[85, 70, 95,60]}
df = pd.DataFrame(data)

# Creating a new column with categorical data
df['Performance'] = pd.cut(df['Score'], bins=[0, 70, 90, 100], labels=['Poor','Average','Excellent'])
print('DataFrame with Categorical Performance:\n', df)

'''
Use cut when you need to segment and sort data values into bins
Pandas cut() function is used to separate the array elements into different bins
'''

'''
Example 1: Let’s say we have an array of 10 random numbers from 1 to 100 and we wish to separate data into 5 bins of (1,20] , (20,40] , (40,60] ,  (60,80] , (80,100] .

'''
import numpy as np
df2 = pd.DataFrame({'Number': np.random.randint(1, 100, 10)})
df2['bins'] = pd.cut(x=df2['Number'], bins = [1, 20, 40, 60, 80, 100])

print('DataFrame 2 :\n',df2)

# We can check the frequency of each bin
print(df2['bins'].unique())



import pandas as pd
import numpy as np
 
df3 = pd.DataFrame({'number': np.random.randint(1, 100, 10)})
df3['bins'] = pd.cut(x=df3['number'], bins=[1, 20, 40, 60, 80, 100],
                    labels=['1 to 20', '21 to 40', '41 to 60',
                            '61 to 80', '81 to 100'])
 
print(df3)
 
# We can check the frequency of each bin
print(df3['bins'].unique())