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
import resources



#The Flask app is located at this file
app = Flask(__name__)

#Persistent variables, won't be deleted between requests
engine = db.engine()
meta = db.meta(engine)
tables = db.tables(engine, meta)
item_methods = ["GET", "PUT", "PATCH", "DELETE"]
list_methods = ["GET", "PUT", "PATCH", "DELETE", "POST"]

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

#Private: Show navigation menu
@app.route("/v1/data/menu")
def app_menu():
    route_list = [
        "/v1/data/gym/excercises",
        "/v1/data/gym/musclegroups",
        "/v1/data/gym/routines",
        "/v1/data/gym/sets",
        "/v1/data/gym/workouts",
    ]

    html = ""
    for route in route_list:
        html += '<a target="_blank" href="{}">{}</a></br>'.format(route, route)

    return html

@app.route("/v1/data/gym/excercises/", defaults={'id':None}, methods=list_methods)
@app.route("/v1/data/gym/excercises/<id>", methods=item_methods)
def gym_excercises(id):

    #Initialize database connection
    conn = db()

    #Process request
    processor  = resources.GymExcercise(conn, engine, meta, request, id)
    response = processor.process()

    return response

@app.route("/v1/data/gym/musclegroups/", defaults={'id':None}, methods=list_methods)
@app.route("/v1/data/gym/musclegroups/<id>", methods=item_methods)
def gym_musclegroups(id):

    #Initialize database connection
    conn = db()

    #Process request
    processor  = resources.GymMuscleGroup(conn, engine, meta, request, id)
    response = processor.process()

    return response

@app.route("/v1/data/gym/routines/", defaults={'id':None}, methods=list_methods)
@app.route("/v1/data/gym/routines/<id>", methods=item_methods)
def gym_routines(id):

    #Initialize database connection
    conn = db()

    #Process request
    processor  = resources.GymRoutine(conn, engine, meta, request, id)
    response = processor.process()

    return response

@app.route("/v1/data/gym/sets/", defaults={'id':None}, methods=list_methods)
@app.route("/v1/data/gym/sets/<id>", methods=item_methods)
def gym_sets_object(id):

    #Initialize database connection
    conn = db()

    #Process request
    processor  = resources.GymSet(conn, engine, meta, request, id)
    response = processor.process()

    return response


@app.route("/v1/data/gym/workouts/", defaults={'id':None}, methods=list_methods)
@app.route("/v1/data/gym/workouts/<id>", methods=item_methods)
#@app.route("/v1/data/gym/workouts/<id>", methods=list_methods)
def gym_workouts(id):

    #Initialize database connection
    conn = db()

    #Process request
    processor  = resources.GymWorkout(conn, engine, meta, request, id)
    response = processor.process()

    return response



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
    app.run(host='0.0.0.0', port=8001, debug=True)
