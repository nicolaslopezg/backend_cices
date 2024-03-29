from re import M
import string
from urllib import response
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
import random

from fastapi_sqlalchemy import db, DBSessionMiddleware
from model import *

model.Base.metadata.create_all(bind=engine)
model.Base.metadata.schema = 'info_db'

#Se inicializa la aplicación

app = FastAPI()

#Se indican los endpoints a los que debe responder desde el frontend

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Se realiza la conexión pertinente a la bsae de datos

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

#Query normal
@app.get('/section/')
async def section():
    section = db.session.query(Section).all()
    print(db.session.query(Section))
    return section

#Query ocultando datos
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

#Query normal
@app.get('/enrollment/')
async def enrollment():
    enrollment = db.session.query(Enrollment).all()
    print(db.session.query(Enrollment))
    return enrollment

#Query ocultando datos
@app.get('/enrollment_hide/')
async def enrollment():
    enrollment = db.session.query(Enrollment).all()
    for element in enrollment:
        element.student_id = "*"
        element.sec_id = "*"
    print(db.session.query(Enrollment))
    return enrollment

#Query normal
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

#Query normal
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

#Query normal
@app.get('/course/')
async def course():
    course = db.session.query(Course).all()
    print(db.session.query(Course))
    return course

#Query ocultando datos
@app.get('/course_hide/')
async def course():
    course = db.session.query(Course).all()
    for element in course:
        element.crs_id = "*"
        element.crs_title = functions.codificar(element.crs_title,7)
    print(db.session.query(Course))
    return course

#############################################################
# Info todas las tablas por cada columnas segun se solicite #
#############################################################

#Tabla cursos
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

#Tabla estudiantes
@app.get('/student_columns/')
async def info_db():
    columnas = []
    nombres = ['ID', 'Nombre','Apellido','Promedio','Año ingreso','Semestre ingreso','ID carrera','Comuna','Quintil']
    i=0
    inspector = inspect(engine)
    for column in inspector.get_columns("student"):
        columnas.append(nombres[i])
        columnas.append(column['name'])
        i=i+1
    return columnas

#Tabla secciones
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

#Tabla profesores
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

#Tabla roles
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

#Tabla centros educativos
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

#Tabla departamentos
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

#############################################################
# Info de los nombres de las columnas de la base de datos   #
#############################################################
@app.get('/info_db/')
async def info_db():
    nombres = ['Cursos','Departamento','Centro educacional','Rol','Profesor','Seccion','Estudiante']
    return nombres

@app.get('/info_db_columnas/')
async def info_db():
    cursos = ['ID curso','Nombre asignatura','Créditos','ID departamento']
    departamento = ['ID departamento','Nombre departamento']
    centro_ed = ['ID centro','Nombre centro','País centro']
    rol = ['ID estudiante','ID seccion']
    profesor = ['ID profesor','Nombre','Apellido']
    seccion = ['ID seccion','ID curso','N° seccion','ID centro','ID profesor']
    estudiante = ['ID estudiante','Nombre','Apellido','Promedio','Año ingreso','Semestre ingreso','ID carrera','Comuna','Quintil']
    columnas = [cursos,departamento,centro_ed,rol,profesor,seccion,estudiante]
    return columnas


#############################################################
# Endpoint que busca un elemento en especifico de una tabla #
#############################################################
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
            if nombre_atributo == 'ID estudiante':
                columna.append(item.student_id)
            elif nombre_atributo == 'Nombre':
                columna.append(item.student_fname)
            elif nombre_atributo == 'Apellido':
                columna.append(item.student_lname)
            elif nombre_atributo == 'Promedio':
                columna.append(item.student_gpa)
            elif nombre_atributo == 'Año ingreso':
                columna.append(item.student_entryYear)
            elif nombre_atributo == 'Semestre ingreso':
                columna.append(item.student_entrySemester)
            elif nombre_atributo == 'ID carrera':
                columna.append(item.student_carreerId)
            elif nombre_atributo == 'Comuna':
                columna.append(item.student_commune)
            elif nombre_atributo == 'Quintil':
                columna.append(item.student_quintile)

    ######################Cursos########################
    elif(nombre_tabla=='Cursos'):
        for item in course:
            if nombre_atributo == 'ID curso':
                columna.append(item.crs_id)
            elif nombre_atributo == 'Nombre asignatura':
                columna.append(item.crs_title)
            elif nombre_atributo == 'Créditos':
                columna.append(item.crs_credits)
            elif nombre_atributo == 'ID departamento':
                columna.append(item.dep_id)

    ######################Departamentos##################
    elif(nombre_tabla=='Departamento'):
        for item in department:
            if nombre_atributo == 'ID departamento':
                columna.append(item.dep_id)
            elif nombre_atributo == 'Nombre departamento':
                columna.append(item.dep_name)

    ######################Ed center####################
    elif(nombre_tabla=='Centro Educacional'):
        for item in ed_center:
            if nombre_atributo == 'ID centro':
                columna.append(item.edc_id)
            elif nombre_atributo == 'Nombre centro':
                columna.append(item.edc_name)
            elif nombre_atributo == 'País centro':
                columna.append(item.edc_country)

    ########################Rol########################
    elif(nombre_tabla=='Rol'):
        for item in enrollment:
            if nombre_atributo == 'ID estudiante':
                columna.append(item.student_id)
            elif nombre_atributo == 'ID seccion':
                columna.append(item.sec_id)

    ######################Profesor########################
    elif(nombre_tabla=='Profesor'):
        for item in instructor:
            if nombre_atributo == 'ID profesor':
                columna.append(item.ins_id)
            elif nombre_atributo == 'Nombre':
                columna.append(item.ins_fname)
            elif nombre_atributo == 'Apellido':
                columna.append(item.ins_lname)

    ####################Seccion###########################
    elif(nombre_tabla=='Seccion'):
        for item in section:
            if nombre_atributo == 'ID seccion':
                columna.append(item.sec_id)
            elif nombre_atributo == 'ID curso':
                columna.append(item.crs_id)
            elif nombre_atributo == 'N° seccion':
                columna.append(item.sec_num)
            elif nombre_atributo == 'ID centro':
                columna.append(item.edc_id)
            elif nombre_atributo == 'ID profesor':
                columna.append(item.ins_id)
    return columna

###############################################################
# Endpoint para agregar datos a la base de datos              #
# en específico se agrega las acciones realizada a los datos  #
# tales como tipo de cifrado                                  #
###############################################################

#Post proyectos
@app.post('/project/{name}/{id}')
def create_project(id:int,name:str):
    new_id = int(id)
    new_project = Project(project_id=new_id,project_name=name)
    db.session.add(new_project)
    db.session.commit()
    return new_project

#Post acciones
@app.post('/project/{id}/{tabla}/{atribute}/{action}/{id_proyecto}')
def create_project(id:int,tabla:str,atribute:str,action:str,id_proyecto:int):
    new_id = int(id)
    new_id_proyecto = int(id_proyecto)
    new_action = Action(action_id=new_id,tabla_mod=tabla,atribute_mod=atribute,action_mod=action,project_id=new_id_proyecto)
    db.session.add(new_action)
    db.session.commit()
    return new_action

#############################################################
# Info de otros datos requeridos para el estudiante         #
#############################################################

#query para obtener comunas
@app.get('/communes_list/')
async def communes_list():
    communes_list = []
    student = db.session.query(Student).all()
    ##print(db.session.query(Student))
    for elemento in student:
        communes_list.append(elemento.student_commune)
    return communes_list

#query para obtener años de ingreso
@app.get('/entryYear_list/')
async def entryYear_list():
    entryYear_list = []
    student = db.session.query(Student).all()
    for elemento in student:
        entryYear_list.append(elemento.student_entryYear)
    return entryYear_list

#query para obtener quintiles
@app.get('/quintile_list/')
async def quintile_list():
    quintile_list = []
    student = db.session.query(Student).all()
    for elemento in student:
        quintile_list.append(elemento.student_quintile)
    return quintile_list

#query para obtener semestre ingreso
@app.get('/entrySemester_list/')
async def entrySemester_list():
    entrySemester_list = []
    student = db.session.query(Student).all()
    for elemento in student:
        entrySemester_list.append(elemento.student_entrySemester)
    return entrySemester_list

#query para obtener promedio
@app.get('/gpa_list/')
async def gpa_list():
    gpa_list = []
    student = db.session.query(Student).all()
    for elemento in student:
        gpa_list.append(elemento.student_gpa)
    return gpa_list



#############################################################
# Info de los datos condicionando un filtro de por medio    #
#############################################################

@app.get('/filter/')
async def filter():
    filter = db.session.query(Filter).all()
    print(db.session.query(Filter))
    return filter

@app.get('/filter_list/')
async def filter_list():
    filter_list = []
    filter = db.session.query(Filter).all()
    print(db.session.query(Filter))
    for elemento in filter:
        if(elemento.option != 0):
            filter_list.append(elemento.table_id)
    return filter_list