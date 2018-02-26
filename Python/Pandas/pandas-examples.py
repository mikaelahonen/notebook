import numpy as np
import pandas as pd

#Create series
group = pd.Series(["A","B","C","A","B","B","A"])
income = pd.Series([5000,2000,4000,3000,1500,1000,4500])

#Series to data frame
df = pd.DataFrame()
df['group'] = group
df['income'] = income

print(df)

#Rank by group
df_rank = df.groupby("group")["income"].rank(method="dense")

#Glue rank to original data frame
print(pd.concat([df, df_rank], axis=1))
