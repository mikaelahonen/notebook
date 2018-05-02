from sqlalchemy.sql import *
from sqlalchemy import Table
from custom import *
import time
import json

class RequestCore(object):

    #Initialize the class
    def __init__(self, db, engine, meta, request, id=None):
        self.request = request
        self.db = db
        self.meta = meta
        self.engine = engine
        self.id = id
        #self.table_name has to be defined in child class before calling super()
        self.table = Table(self.table_name, self.meta, autoload=True, autoload_with=self.engine)

    def query_template(self, base_query, order_list, where_list):

        order = ", ".join(order_list)
        where = " AND ".join(where_list)

        query = '''
            SELECT *
            FROM(
                SELECT *, ROW_NUMBER() OVER(ORDER BY {}) AS row_number
                FROM(
                    {}
                ) AS tbl_calc
            ) AS tbl_rank
            WHERE {}
        '''.format(order, base_query, where)

        return query

    def http_get(self):

        params = {}

        #Override template values from child, if exists
        base_query = "select * from {}".format(self.table_name)
        if hasattr(self, "base_query"):
            base_query = self.base_query

        order = ["id"]
        if hasattr(self, "template_order"):
            order = self.template_order

        where = ["1=1"]
        if hasattr(self, "template_where"):
            where = self.template_where

        #Filter by first row
        if self.request.args.get('rows_first') is None:
            rows_first = 1
        else:
            rows_first = self.request.args.get('rows_first')
            rows_first = int(rows_first)
            params["rows_first"] = rows_first
            where.append("row_number >= %(rows_first)s")

        #Filter by last row
        if self.request.args.get('rows_total') == 0:
            pass
        else:
            if self.request.args.get('rows_total') is None:
                rows_total = 50
            else:
                rows_total = self.request.args.get('rows_total')
                rows_total = int(rows_total)

            rows_last = rows_first + rows_total - 1
            params["rows_last"] = rows_last
            where.append("row_number <= %(rows_last)s")

        #Filter by id
        if self.id is None:
            print("No id")
            pass
        else:
            print("id: " + str(self.id))
            params["id"] = int(self.id)
            where.append("id=%(id)s")

        #Order by
        if self.request.args.get('sort') is None:
            pass
        else:
            order = []
            sort_list = self.request.args.get('sort').split(",")
            #Sanitize by regex
            for sort in sort_list:

                #If first letter is dash > DESC
                isDesc = sort[:1]=="-"

                #DESC
                if isDesc:
                    condition = sort[1:]
                    direction = "DESC"
                #ASC
                else:
                    condition = sort
                    direction = "ASC"

                order.append(condition + " " + direction)


        query = self.query_template(base_query, order, where)
        print(params)
        print(query)

        df = pd.read_sql_query(
            sql=query,
            con=self.db,
            params=params
        )

        return df

    def http_post(self):

        #Create a data frame from post data
        try:
            #Read json data to dict
            dict_data = self.request.get_json()
            #Use list() to indicate there's just one row
            df = pd.DataFrame(list(dict_data))
        except Exception as e:
            error_response = {"Error": str(e)}
            return error_response

        try:
            db_insert = df.to_sql(
                name=self.table_name,
                if_exists="append",
                index=False, #Do not write index as a column
                con=self.db
            )
            print(db_insert)
        except Exception as e:
            error_response = {"Error": str(e)}
            return error_response

        return dict_data

    def http_put(self):
        return '{"Msg":"Not implemented"}'

    def http_patch(self):
        return '{"Msg":"Not implemented"}'

    def http_delete(self):
        return '{"Msg":"Not implemented"}'

    #Recognize http method and return pandas data frame
    def base(self):

        #Return data
        if self.request.method == "GET":
            return self.http_get()

        #Create new
        elif self.request.method == 'POST':
            return self.http_post()

        #Update all fields of existing object.
        elif self.request.method == 'PUT':
            return self.http_put()

        #Update existing object partially.
        elif self.request.method == 'PATCH':
            return self.http_patch()

        elif self.request.method == 'DELETE':
            return self.http_delete()

        else:
            return None
