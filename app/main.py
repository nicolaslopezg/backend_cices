from re import M
from fastapi import FastAPI
from sqlalchemy import MetaData
import model
from config import engine, DATABASE_URL
import router
import os
import pandas as pd
import functions
from fastapi.middleware.cors import CORSMiddleware

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

app.include_router(router.router,prefix="/student",tags=["student"])


# app.include_router(router.router,prefix="/categoria",tags=["categoria"])

# app.include_router(router.router,prefix="/alumno_car",tags=["alumno_car"])


# @app.get('/alumno_car/')
# async def alumno_car():
#     alumno_car = db.session.query(Alumno_car).all()
#     print('entre aca')
#     return alumno_car

# #Alumno_car escondiendo rut
# @app.get('/alumno_car_data/')
# async def alumno_car_data():
#     alumno_car_data = db.session.query(Alumno_car).all()
#     for element in alumno_car_data:
#         element.alu_rut = "*********"
#         element.alu_paterno = functions.codificar(element.alu_paterno,7)
#         element.alu_e_mail = functions.codificar(element.alu_e_mail,7)
#         element.alu_e_mail2 = functions.codificar(element.alu_e_mail2,7)
#         print(element)
#     return alumno_car_data

# @app.get('/categoria/')
# async def categoria():
#     categoria = db.session.query(Categoria).all()
#     print(db.session.query(Categoria))
#     return categoria

# @app.get('/asignatura/')
# async def asignatura():
#     asignatura = db.session.query(Asignatura).all()
#     print(db.session.query(Asignatura))
#     return asignatura

# @app.get('/comuna/')
# async def comuna():
#     comuna = db.session.query(Comuna).all()
#     print(db.session.query(Comuna))
#     return comuna


# @app.get('/curso/')
# async def curso():
#     curso = db.session.query(Curso).all()
#     print(db.session.query(Curso))
#     return curso


#Query normal
@app.get('/student/')
async def student():
    student = db.session.query(Student).all()
    print(db.session.query(Student))
    return student

#Query ocultando datos
@app.get('/student_hide/')
async def student():
    student = db.session.query(Student).all()
    for element in student:
        element.student_id = "*"
        element.student_lname = functions.codificar(element.student_lname,7)
    print(db.session.query(Student))
    return student

@app.get('/section/')
async def section():
    section = db.session.query(Section).all()
    print(db.session.query(Section))
    return section

#Query normal
@app.get('/instructor/')
async def instructor():
    instructor = db.session.query(Instructor).all()
    print(db.session.query(Instructor))
    return instructor

#Query ocultando datos
@app.get('/instructor_hide/')
async def instructor():
    instructor = db.session.query(Instructor).all()
    for element in instructor:
        element.ins_id = "*"
        element.ins_lname = functions.codificar(element.ins_lname,7)
    print(db.session.query(Instructor))
    return instructor


@app.get('/enrollment/')
async def enrollment():
    enrollment = db.session.query(Enrollment).all()
    print(db.session.query(Enrollment))
    return enrollment

@app.get('/ed_center/')
async def ed_center():
    ed_center = db.session.query(Ed_center).all()
    print(db.session.query(Ed_center))
    return ed_center

#Query ocultando datos
@app.get('/ed_center_hide/')
async def ed_center():
    ed_center = db.session.query(Ed_center).all()
    for element in ed_center:
        element.edc_id = "*"
        element.edc_name = functions.codificar(element.edc_name,7)
    print(db.session.query(Ed_center))
    return ed_center

@app.get('/department/')
async def department():
    department = db.session.query(Department).all()
    print(db.session.query(Department))
    return department

#Query ocultando datos
@app.get('/department_hide/')
async def department():
    department = db.session.query(Department).all()
    for element in department:
        element.dep_id = "*"
        element.dep_name = functions.codificar(element.dep_name,7)
    print(db.session.query(Department))
    return department

@app.get('/course/')
async def course():
    course = db.session.query(Course).all()
    print(db.session.query(Course))
    return course

@app.get('/course_hide/')
async def course():
    course = db.session.query(Course).all()
    for element in course:
        element.crs_id = "*"
        element.crs_title = functions.codificar(element.crs_title,7)
    print(db.session.query(Course))
    return course