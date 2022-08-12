from venv import create
from sqlalchemy import create_engine
from sshtunnel import SSHTunnelForwarder
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#Conexión a la base de datos con los datos necesarios
DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/cices_test"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

print('connect to db')