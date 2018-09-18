from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Model1(Base):

    #Table name
    __tablename__ = 'test_table'

    #Columns
    id = Column(Integer, primary_key=True)
    name = Column(String)
    str_column = Column(String)

    #Representation
    def __repr__(self):
       return "<User(name='%s', id='%s')>" % (
                            self.name, self.id)
