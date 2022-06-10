from turtle import title
from sqlalchemy import Column, Integer, SmallInteger, String
from config import Base
import functions

# class Book(Base):
#     __tablename__ = 'book'

#     id=Column(Integer, primary_key=True)
#     title=Column(String)
#     description=Column(String)


# class Categoria(Base):
#     __tablename__ = 'categoria'

#     cat_codigo=Column(SmallInteger, primary_key=True)
#     cat_descrip=Column(String)

#     __table_args__ = {'schema': 'info_db'}

    
# class Alumno_car(Base):
#     __tablename__ = 'alumno_car'

#     alu_rut = Column(Integer, primary_key=True)
#     alu_dv = Column(String)
#     alu_paterno = Column(String)
#     alu_materno = Column(String)
#     alu_nombre = Column(String)
#     alu_sexo = Column(String)
#     alu_direc_stgo = Column(String)
#     alu_comuna = Column(Integer)
#     alu_region = Column(Integer)
#     alu_region = Column(Integer)
#     alu_sit_mili = Column(Integer)
#     alu_fecha_nac = Column(Integer)
#     alu_nacionalidad = Column(Integer)
#     alu_pais = Column(String)
#     alu_fono = Column(String)
#     alu_est_civ = Column(Integer)
#     alu_pass = Column(String)
#     alu_e_mail = Column(String)
#     alu_direc_fam = Column(String)
#     alu_comuna_fam = Column(String)
#     alu_fono_fam = Column(String)
#     alu_e_mail2 = Column(String)
#     alu_celular = Column(String)
#     aca_rut = Column(String)

#     __table_args__ = {'schema': 'info_db'}


# class Asignatura(Base):
#     __tablename__ = 'asignatura'

#     asi_cod=Column(Integer, primary_key=True)
#     asi_nom=Column(String)
#     asi_teo=Column(SmallInteger)
#     asi_ejer=Column(SmallInteger)
#     asi_lab=Column(SmallInteger)

#     __table_args__ = {'schema': 'info_db'}


# class Comuna(Base):
#     __tablename__ = 'comuna'

#     com_cod=Column(Integer, primary_key=True)
#     com_nom=Column(String)
#     com_reg_cod=Column(Integer)
#     com_cod_ofi=Column(Integer)

#     __table_args__ = {'schema': 'info_db'}

# class Curso(Base):
#     __tablename__ = 'curso'

#     cur_asign=Column(Integer, primary_key=True)
#     cur_elect=Column(String)
#     cur_coord=Column(String)
#     cur_agno=Column(SmallInteger)
#     cur_sem=Column(SmallInteger)

#     __table_args__ = {'schema': 'info_db'}

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