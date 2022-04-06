from re import M
from fastapi import FastAPI
from sqlalchemy import MetaData
from sqlalchemy import inspect
import model
from config import engine, DATABASE_URL
import router
import os
import pandas as pd
import functions
from fastapi.middleware.cors import CORSMiddleware
import json

from fastapi_sqlalchemy import db, DBSessionMiddleware
from model import *

model.Base.metadata.create_all(bind=engine)
model.Base.metadata.schema = 'info_db'

app = FastAPI()

origins = [
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

os.environ['DATABASE_URL'] = DATABASE_URL

app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])


@app.get('/')
async def Home():
    return "Welcome Home"

app.include_router(router.router,prefix="/book",tags=["book"])


# app.include_router(router.router,prefix="/categoria",tags=["categoria"])

# app.include_router(router.router,prefix="/alumno_car",tags=["alumno_car"])


@app.get('/alumno_car/')
async def alumno_car():
    alumno_car = db.session.query(Alumno_car).all()
    print('entre aca')
    return alumno_car

#Alumno_car escondiendo rut
@app.get('/alumno_car_data/')
async def alumno_car_data():
    alumno_car_data = db.session.query(Alumno_car).all()
    for element in alumno_car_data:
        element.alu_rut = "*********"
        element.alu_paterno = functions.codificar(element.alu_paterno,7)
        element.alu_e_mail = functions.codificar(element.alu_e_mail,7)
        element.alu_e_mail2 = functions.codificar(element.alu_e_mail2,7)
        print(element)
    return alumno_car_data

@app.get('/categoria/')
async def categoria():
    categoria = db.session.query(Categoria).all()
    print(db.session.query(Categoria))
    return categoria

@app.get('/asignatura/')
async def asignatura():
    asignatura = db.session.query(Asignatura).all()
    print(db.session.query(Asignatura))
    return asignatura

@app.get('/comuna/')
async def comuna():
    comuna = db.session.query(Comuna).all()
    print(db.session.query(Comuna))
    return comuna


@app.get('/info_db/')
async def info_db():
    inspector = inspect(engine)
    schemas = inspector.get_table_names(schema="info_db")
    return schemas

@app.get('/info_db_columnas/')
async def info_db():
    columnas = []
    total_columnas = []
    inspector = inspect(engine)
    schemas = inspector.get_table_names(schema="info_db")
    for table_name in schemas:
        for column in inspector.get_columns(table_name, schema="info_db"):
            columnas.append(column['name'])
        total_columnas.append(columnas)
        columnas = []
    return total_columnas
