from sqlalchemy.sql import *
from custom import *

class RequestCore:

    #Initialize the class
    def __init__(self, db, request, table):
        self.request = request
        self.table = table
        self.db = db
        print("init")

    def http_get(self):

        q = select([self.table])

        #Filters

        #Order by

        params = {}

        df = pd.read_sql_query(
            sql=q,
            con=self.db,
            params=params
        )

        return df_response(df)

    def process(self):

        if self.request.method == "GET":
            return self.http_get()

        elif self.request.method == 'POST':
            #create new
            pass

        elif self.request.method == 'PUT':
            #update all
            pass

        elif self.request.method == 'PATCH':
            #update partial
            pass

        else:
            #if somthing went wrong
            return None
