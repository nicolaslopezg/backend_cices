from dataclasses import field
from re import S
from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel
from sqlalchemy import SMALLINT, Integer, SmallInteger

T = TypeVar('T')

# class BookSchema(BaseModel):
#     id: Optional[int]=None
#     title: Optional[str]=None
#     description: Optional[str]=None

#     class Config:
#         orm_mode = True

# class RequestBook(BaseModel):
#     parameter: BookSchema = Field(...)

# class Response (GenericModel, Generic[T]):
#     code: str
#     status: str
#     message: str
#     result: Optional[T]

# #NEW
# class CategoriaSchema(BaseModel):
#     cat_codigo: Optional[int]=None
#     cat_descrip: Optional[str]=None

#     class Config:
#         orm_mode = True
    
# class RequestCategoria(BaseModel):
#     parameter: CategoriaSchema = Field(...)


# #NEW
# class Alumno_carSchema(BaseModel):
#     alu_rut: Optional[int]=None
#     alu_dv: Optional[str]=None
#     alu_paterno: Optional[str]=None
#     alu_materno: Optional[str]=None
#     alu_nombre: Optional[str]=None
#     alu_sexo: Optional[str]=None
#     alu_direc_stgo: Optional[str]=None
#     alu_comuna: Optional[int]=None
#     alu_region: Optional[int]=None
#     alu_region: Optional[int]=None
#     alu_sit_mili: Optional[int]=None
#     alu_fecha_nac: Optional[int]=None
#     alu_nacionalidad: Optional[int]=None
#     alu_pais: Optional[str]=None
#     alu_fono: Optional[str]=None
#     alu_est_civ: Optional[int]=None
#     alu_pass: Optional[str]=None
#     alu_e_mail: Optional[str]=None
#     alu_direc_fam: Optional[str]=None
#     alu_comuna_fam: Optional[str]=None
#     alu_fono_fam: Optional[str]=None
#     alu_e_mail2: Optional[str]=None
#     alu_celular: Optional[str]=None
#     aca_rut: Optional[str]=None

#     class Config:
#         orm_mode = True
    
# class RequestAlumno_car(BaseModel):
#     parameter: Alumno_carSchema = Field(...)

# #NEW
# class AsignaturaSchema(BaseModel):
#     asi_cod: Optional[int] = None
#     asi_nom: Optional[str] = None
#     asi_teo: Optional[int] = None
#     asi_ejer: Optional[int] = None
#     asi_lab: Optional[int] = None

#     class Config:
#         orm_mode = True
    
# class RequestAsignatura(BaseModel):
#     parameter: AsignaturaSchema = Field(...)
    
# #NEW
# class ComunaSchema(BaseModel):
#     com_cod: Optional[int] = None
#     com_nom: Optional[str] = None
#     com_reg_cod: Optional[int] = None
#     com_cod_ofi: Optional[int] = None

#     class Config:
#         orm_mode = True
    
# class RequestComuna(BaseModel):
#     parameter: ComunaSchema = Field(...)

# class CursoSchema(BaseModel):
#     cur_asign: Optional[int] = None
#     cur_elect: Optional[str] = None
#     cur_coord: Optional[str] = None
#     cur_agno: Optional[int] = None
#     cur_sem: Optional[int] = None

#     class Config:
#         orm_mode = True
    
# class RequestCurso(BaseModel):
#     parameter: CursoSchema = Field(...)

#NEW student
class StudentSchema(BaseModel):
    student_id: Optional[int] = None
    student_fname: Optional[str] = None
    student_lname: Optional[str] = None
    student_gpa: Optional[int] = None

    class Config:
        orm_mode = True
    
class RequestStudent(BaseModel):
    parameter: StudentSchema = Field(...)

#NEW section
class SectionSchema(BaseModel):
    sec_id: Optional[int] = None
    crs_id: Optional[int] = None
    sec_num: Optional[int] = None
    edc_id: Optional[int] = None
    ins_id: Optional[int] = None

    class Config:
        orm_mode = True
    
class RequestSection(BaseModel):
    parameter: SectionSchema = Field(...)

#NEW instructor
class InstructorSchema(BaseModel):
    ins_id: Optional[int] = None
    ins_fname: Optional[str] = None
    ins_lname: Optional[str] = None

    class Config:
        orm_mode = True
    
class RequestInstructor(BaseModel):
    parameter: InstructorSchema = Field(...)

#NEW enrollment
class EnrollmentSchema(BaseModel):
    student_id: Optional[int] = None
    sec_id: Optional[int] = None

    class Config:
        orm_mode = True
    
class RequestEnrollment(BaseModel):
    parameter: EnrollmentSchema = Field(...)

#NEW education center
class EducationCenterSchema(BaseModel):
    edc_id: Optional[int] = None
    edc_name: Optional[str] = None
    edc_country: Optional[str] = None

    class Config:
        orm_mode = True
    
class RequestEducationCenter(BaseModel):
    parameter: EducationCenterSchema = Field(...)

#NEW department
class DepartmentSchema(BaseModel):
    dep_id: Optional[int] = None
    dep_name: Optional[str] = None

    class Config:
        orm_mode = True
    
class RequestDepartment(BaseModel):
    parameter: DepartmentSchema = Field(...)

#NEW course
class CourseSchema(BaseModel):
    crs_id: Optional[int] = None
    crs_title: Optional[str] = None
    crs_credits: Optional[str] = None
    dep_id: Optional[int] = None

    class Config:
        orm_mode = True
    
class RequestCourse(BaseModel):
    parameter: CourseSchema = Field(...)

#NEW project
class ProjectSchema(BaseModel):
    project_id: Optional[int] = None
    project_name: Optional[str] = None

    class Config:
        orm_mode = True
    
class RequestProject(BaseModel):
    parameter: ProjectSchema = Field(...)

#NEW action
class ActionSchema(BaseModel):
    action_id: Optional[int] = None
    tabla_mod: Optional[str] = None
    atribute_mod: Optional[str] = None
    action_mod: Optional[str] = None
    project_id: Optional[int] = None

    class Config:
        orm_mode = True
    
class RequestAction(BaseModel):
    parameter: ActionSchema = Field(...)