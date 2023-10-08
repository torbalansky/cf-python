# Import necessary modules from SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create an SQLAlchemy engine to connect to the MySQL DB
engine = create_engine("mysql://cf-python:password@localhost/task_database")

# Create a Session class that binds to the DB engine
Session = sessionmaker(bind=engine)

# Create a session object, which will be used for DB interactions
session = Session()
