import numpy as np
import pandas as pd

#Create group and value lists
grp = ["A","A","B","B","C","C"]
val = [1,2,3,4,5,6]

#Data frame from lists
df = pd.DataFrame({'grp':grp, 'val':val})
#Sum of groups
group_sums = df.groupby(['grp']).sum()

print(df)
print(group_sums)
