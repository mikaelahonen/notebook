from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import data_model
import config

conn_str = 'postgresql://' + config.user + ':' + config.pw + '@' + config.host + ':' + config.port + '/' + config.db
engine = create_engine(conn_str)

Session = sessionmaker(bind=engine)

#conn = engine().connect()

#Create table from model
engine = engine()
data_model.Base.metadata.create_all(engine)
