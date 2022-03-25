from re import M
from fastapi import FastAPI
from sqlalchemy import MetaData
import model
from config import engine, DATABASE_URL
import router
import os
import pandas as pd
import functions

from fastapi_sqlalchemy import db, DBSessionMiddleware
from model import *

model.Base.metadata.create_all(bind=engine)
model.Base.metadata.schema = 'info_db'

app = FastAPI()

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


@app.get('/curso/')
async def curso():
    curso = db.session.query(Curso).all()
    print(db.session.query(Curso))
    return curso

