import numpy as np
import pandas as pd
df = pd.DataFrame(np.random.randint(0,100,size=(100, 4)), columns=list('ABCD'))
print(df[1:10])
