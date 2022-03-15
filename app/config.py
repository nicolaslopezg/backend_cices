from venv import create
from sqlalchemy import create_engine
from sshtunnel import SSHTunnelForwarder
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

server = SSHTunnelForwarder(
    ('158.170.35.170', 22),
    ssh_username = "username",
    ssh_password = "password",
    remote_bind_address = ('localhost', 5432)
)


server.start()
local_port = str(server.local_bind_port)
print(local_port)


#DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/python_db"
DATABASE_URL = "postgresql://userdb:passdb@localhost:{}/CS_Dev".format(local_port)


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

print('connect to db')