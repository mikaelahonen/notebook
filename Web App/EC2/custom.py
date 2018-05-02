import pandas as pd
import json

def json_response(data):

    #If data frame: Convert to dict
    if isinstance(data, pd.DataFrame):
        d = data.to_dict('records')
    #Else: Expect dictionary
    else:
        d = data

    j = json.dumps(d, indent=4, default=str)

    return j
