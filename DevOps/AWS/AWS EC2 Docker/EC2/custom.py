import pandas as pd
import json

def df_response(df):
    d = df.to_dict('records')
    j = json.dumps(d, indent=4, default=str)
    return j
