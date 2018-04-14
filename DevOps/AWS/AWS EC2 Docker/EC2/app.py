#App
from flask import Flask, request, g, redirect
from sqlalchemy import create_engine
from sqlalchemy.sql import *
#import psycopg2
#Calculations
import statistics as stats
import pandas as pd
import time
#Custom modules
import config
import db
from custom import *
import requestcore
import gym_workout



#The Flask app is located at this file
app = Flask(__name__)

#Persistent variables, won't be deleted between requests
engine = db.engine()
meta = db.meta(engine)
tables = db.tables(engine, meta)

#Use this function to connect to database
def db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = engine.connect()
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.before_request
def before_request():
    request.start = time.time()

@app.teardown_request
def teardown_request(exception):
    request.end = time.time()
    duration = (request.end-request.start)*1000
    print("Request duration: " + str(int(duration)) + " ms")
    pass


@app.route("/v1/data/gym/workouts")
def gym_workouts():

    #Get required variables
    table = tables["gym_workout"]
    conn = db()

    #Process request
    processor  = gym_workout.GymWorkout(conn, request, table)
    response = processor.process()

    return response
    #tbl_name =
    #tbl = tables[tbl_name]

    #if request.method == 'GET':

        #Initially, no params
        #params = {}

        #query = text("SELECT * FROM gym_workout WHERE id<20")
        #q = select([tbl])

        #if request.args.get('first_id'):
        #    q = q.where(tbl.c.id > request.args.get('first_id'))

        #df = pd.read_sql_query(
        #    sql=q,
        #    con=db(),
        #    params=params
        #)

        #Post process data frame
        #df = df.head(5)

        #Return results
        #return df_response(df)


@app.route("/v1/mean/")
def mean():

	n_str = request.args.get('numbers')

	if not n_str:
		return "No 'numbers' parameter given"
	else:
		n_list = n_str.split(',')
		n_list = [int(x) for x in n_list]
		avg = stats.mean(n_list)
		return "Mean for given numbers is: " + str(avg)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
