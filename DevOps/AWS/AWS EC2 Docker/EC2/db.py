from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime
import config

def engine():
    conn_str = 'postgresql://' + config.user + ':' + config.pw + '@' + config.host + ':' + config.port + '/' + config.db
    engine = create_engine(conn_str)
    return engine

def meta(engine):
    return MetaData(bind=engine)

def tables(engine, meta):
    try:
        tbl_list = [
            #"gym_excercise",
            #"gym_musclegroup",
            #"gym_routine",
            #"gym_plan",
            #"gym_routine",
            #"gym_routine_plan",
            #"gym_set",
            #"gym_section",
            #"gym_set",
            "gym_workout",
        ]

        dict = {}
        for tbl in tbl_list:
            dict[tbl] = Table(tbl, meta, autoload=True, autoload_with=engine)

        return dict

    except:
        print("Error. Make sure, you can connect to the database.")
        return None
