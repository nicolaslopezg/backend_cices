from turtle import title
from sqlalchemy import Column, Integer, SmallInteger, String
from config import Base
import functions

#############################################################
# Modelos para cada tabla utilziada en la base de datos     #
#############################################################

class Student(Base):
    __tablename__ = 'student'

    student_id=Column(Integer, primary_key=True)
    student_fname=Column(String)
    student_lname=Column(String)
    student_gpa=Column(Integer)
    ##añoingreso, semestre ingreso, carrera, quintil, comuna
    student_entryYear=Column(Integer)
    student_entrySemester=Column(Integer)
    student_carreerId=Column(Integer)
    student_commune=Column(String)
    student_quintile=Column(String)

class Section(Base):
    __tablename__ = 'section'

    crs_id=Column(Integer, primary_key=True)
    sec_num=Column(Integer)
    edc_id=Column(Integer)
    ins_id=Column(Integer)

class Instructor(Base):
    __tablename__ = 'instructor'

    ins_id=Column(Integer, primary_key=True)
    ins_fname=Column(String)
    ins_lname=Column(String)

class Enrollment(Base):
    __tablename__ = 'enrollment'

    student_id=Column(Integer, primary_key=True)
    sec_id=Column(Integer)

class Ed_center(Base):
    __tablename__ = 'ed_center'

    edc_id=Column(Integer, primary_key=True)
    edc_name=Column(String)
    edc_country=Column(String)

class Department(Base):
    __tablename__ = 'department'

    dep_id=Column(Integer, primary_key=True)
    dep_name=Column(String)

class Course(Base):
    __tablename__ = 'course'

    crs_id=Column(Integer, primary_key=True)
    crs_title=Column(String)
    crs_credits=Column(String)
    dep_id=Column(Integer)

class Project(Base):
    __tablename__ = 'project'

    project_id=Column(Integer, primary_key=True)
    project_name=Column(String)

class Action(Base):
    __tablename__ = 'action'

    action_id=Column(Integer, primary_key=True)
    tabla_mod=Column(String)
    atribute_mod=Column(String)
    action_mod=Column(String)
    project_id=Column(Integer)


class Filter(Base):
    __tablename__ = 'filter'

    table_id = Column(String, primary_key = True)
    option = Column(Integer)