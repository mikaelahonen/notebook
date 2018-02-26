#Clock the time it takes to sort
import numpy as np
import pandas as pd
import datetime

#Get start time
t_start = datetime.datetime.now().time()

#Sort data frame size of million by two conditions
df = pd.DataFrame(np.random.randint(0,1000,size=(1000000, 4)), columns=list('ABCD'))
df = df.sort_values(by=['A', 'B'])

#Get end time
t_end = datetime.datetime.now().time()

#Print results
print(df[1:50])
print(t_start)
print(t_end)
