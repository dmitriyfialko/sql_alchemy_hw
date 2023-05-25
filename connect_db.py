from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('postgresql+psycopg2://postgres:12345@localhost/postgres')
DBSession = sessionmaker(bind=engine)
session = DBSession()
