from re import M
import string
from fastapi import FastAPI
from sqlalchemy import MetaData
from sqlalchemy import inspect
from sqlalchemy.orm import load_only
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

app.include_router(router.router,prefix="/student",tags=["student"])

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

@app.get('/section_hide/')
async def section():
    section = db.session.query(Section).all()
    for element in section:
        element.sec_num = "*"
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

@app.get('/enrollment_hide/')
async def enrollment():
    enrollment = db.session.query(Enrollment).all()
    for element in enrollment:
        element.student_id = "*"
        element.sec_id = "*"
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

#########################
#Info todas las tablas
@app.get('/course_columns/')
async def info_db():
    columnas = []
    nombres = ['ID', 'Nombre','Creditos','ID depto asociado']
    i=0
    inspector = inspect(engine)
    for column in inspector.get_columns("course"):
        columnas.append(nombres[i])
        columnas.append(column['name'])
        i=i+1
    return columnas

@app.get('/student_columns/')
async def info_db():
    columnas = []
    nombres = ['ID', 'Nombre','Apellido','Promedio']
    i=0
    inspector = inspect(engine)
    for column in inspector.get_columns("student"):
        columnas.append(nombres[i])
        columnas.append(column['name'])
        i=i+1
    return columnas

@app.get('/section_columns/')
async def info_db():
    columnas = []
    nombres = ['ID', 'ID Curso','N° Sección','ID Edc','ID Instituto']
    i=0
    inspector = inspect(engine)
    for column in inspector.get_columns("section"):
        columnas.append(nombres[i])
        columnas.append(column['name'])
        i=i+1
    return columnas

@app.get('/instructor_columns/')
async def info_db():
    columnas = []
    nombres = ['ID', 'Nombre','Apellido']
    i=0
    inspector = inspect(engine)
    for column in inspector.get_columns("instructor"):
        columnas.append(nombres[i])
        columnas.append(column['name'])
        i=i+1
    return columnas

@app.get('/enrollment_columns/')
async def info_db():
    columnas = []
    nombres = ['ID Alumno', 'ID Sección']
    i=0
    inspector = inspect(engine)
    for column in inspector.get_columns("enrollment"):
        columnas.append(nombres[i])
        columnas.append(column['name'])
        i=i+1
    return columnas

@app.get('/ed_center_columns/')
async def info_db():
    columnas = []
    nombres = ['ID', 'Nombre','País']
    i=0
    inspector = inspect(engine)
    for column in inspector.get_columns("ed_center"):
        columnas.append(nombres[i])
        columnas.append(column['name'])
        i=i+1
    return columnas

@app.get('/department_columns/')
async def info_db():
    columnas = []
    nombres = ['ID', 'Nombre']
    i=0
    inspector = inspect(engine)
    for column in inspector.get_columns("department"):
        columnas.append(nombres[i])
        columnas.append(column['name'])
        i=i+1
    return columnas

##########################################
@app.get('/info_db/')
async def info_db():
    #inspector = inspect(engine)
    nombres = ['Cursos','Departamento','Centro educacional','Rol','Profesor','Seccion','Estudiante']
    #schemas = inspector.get_table_names(schema="public")
    return nombres

@app.get('/info_db_columnas/')
async def info_db():
    columnas = []
    total_columnas = []
    inspector = inspect(engine)
    schemas = inspector.get_table_names(schema="public")
    for table_name in schemas:
        for column in inspector.get_columns(table_name, schema="public"):
            columnas.append(column['name'])
        total_columnas.append(columnas)
        columnas = []
    return total_columnas

@app.get('/search/{nombre_columna}')
async def read_item(nombre_columna: str):
    columna=[]
    nombre_completo = nombre_columna.split('-')
    nombre_tabla = nombre_completo[0]
    nombre_atributo = nombre_completo[1]

    #Información de tablas
    student = db.session.query(Student).all()
    course = db.session.query(Course).all()
    department = db.session.query(Department).all()
    ed_center = db.session.query(Ed_center).all()
    enrollment = db.session.query(Enrollment).all()
    instructor = db.session.query(Instructor).all()
    section = db.session.query(Section).all()

    #Seccion de encriptacion de parametros
    for element in student:
        element.student_id = "***"
        element.student_lname = functions.codificar(element.student_lname,7)

    for element in section:
        element.sec_num = "***"

    for element in instructor:
        element.ins_id = "***"
        element.ins_lname = functions.codificar(element.ins_lname,7)

    for element in enrollment:
        element.student_id = "***"
        element.sec_id = "***"

    for element in ed_center:
        element.edc_id = "***"
        element.edc_name = functions.codificar(element.edc_name,7)

    for element in department:
        element.dep_id = "*"
        element.dep_name = functions.codificar(element.dep_name,7)
    
    for element in course:
        element.crs_id = "*"
        element.crs_title = functions.codificar(element.crs_title,7)

    ####################Estudiantes##########################
    if(nombre_tabla=='Estudiante'):
        for item in student:
            if nombre_atributo == 'student_id':
                columna.append(item.student_id)
            elif nombre_atributo == 'student_fname':
                columna.append(item.student_fname)
            elif nombre_atributo == 'student_lname':
                columna.append(item.student_lname)
            elif nombre_atributo == 'student_gpa':
                columna.append(item.student_gpa)

    ######################Cursos########################
    elif(nombre_tabla=='Curso'):
        for item in course:
            if nombre_atributo == 'crs_id':
                columna.append(item.crs_id)
            elif nombre_atributo == 'crs_title':
                columna.append(item.crs_title)
            elif nombre_atributo == 'crs_credits':
                columna.append(item.crs_credits)
            elif nombre_atributo == 'dep_id':
                columna.append(item.dep_id)

    ######################Departamentos##################
    elif(nombre_tabla=='Departamento'):
        for item in department:
            if nombre_atributo == 'dep_id':
                columna.append(item.dep_id)
            elif nombre_atributo == 'dep_name':
                columna.append(item.dep_name)

    ######################Ed center####################
    elif(nombre_tabla=='Centro Educacional'):
        for item in ed_center:
            if nombre_atributo == 'edc_id':
                columna.append(item.edc_id)
            elif nombre_atributo == 'edc_name':
                columna.append(item.edc_name)
            elif nombre_atributo == 'edc_country':
                columna.append(item.edc_country)

    ########################Rol########################
    elif(nombre_tabla=='Rol'):
        for item in enrollment:
            if nombre_atributo == 'student_id':
                columna.append(item.student_id)
            elif nombre_atributo == 'sec_id':
                columna.append(item.sec_id)

    ######################Profesor########################
    elif(nombre_tabla=='Profesor'):
        for item in instructor:
            if nombre_atributo == 'ins_id':
                columna.append(item.ins_id)
            elif nombre_atributo == 'ins_fname':
                columna.append(item.ins_fname)
            elif nombre_atributo == 'ins_lname':
                columna.append(item.ins_lname)

    ####################Seccion###########################
    elif(nombre_tabla=='Seccion'):
        for item in section:
            if nombre_columna == 'sec_id':
                columna.append(item.sec_id)
            elif nombre_columna == 'crs_id':
                columna.append(item.crs_id)
            elif nombre_columna == 'sec_num':
                columna.append(item.sec_num)
            elif nombre_columna == 'edc_id':
                columna.append(item.edc_id)
            elif nombre_columna == 'ins_id':
                columna.append(item.ins_id)
    return columna