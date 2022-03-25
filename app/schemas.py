from dataclasses import field
from re import S
from typing import List, Optional, Generic, TypeVar
from pydantic import BaseModel, Field
from pydantic.generics import GenericModel
from sqlalchemy import SMALLINT, Integer, SmallInteger

T = TypeVar('T')

class BookSchema(BaseModel):
    id: Optional[int]=None
    title: Optional[str]=None
    description: Optional[str]=None

    class Config:
        orm_mode = True

class RequestBook(BaseModel):
    parameter: BookSchema = Field(...)

class Response (GenericModel, Generic[T]):
    code: str
    status: str
    message: str
    result: Optional[T]

#NEW
class CategoriaSchema(BaseModel):
    cat_codigo: Optional[int]=None
    cat_descrip: Optional[str]=None

    class Config:
        orm_mode = True
    
class RequestCategoria(BaseModel):
    parameter: CategoriaSchema = Field(...)


#NEW
class Alumno_carSchema(BaseModel):
    alu_rut: Optional[int]=None
    alu_dv: Optional[str]=None
    alu_paterno: Optional[str]=None
    alu_materno: Optional[str]=None
    alu_nombre: Optional[str]=None
    alu_sexo: Optional[str]=None
    alu_direc_stgo: Optional[str]=None
    alu_comuna: Optional[int]=None
    alu_region: Optional[int]=None
    alu_region: Optional[int]=None
    alu_sit_mili: Optional[int]=None
    alu_fecha_nac: Optional[int]=None
    alu_nacionalidad: Optional[int]=None
    alu_pais: Optional[str]=None
    alu_fono: Optional[str]=None
    alu_est_civ: Optional[int]=None
    alu_pass: Optional[str]=None
    alu_e_mail: Optional[str]=None
    alu_direc_fam: Optional[str]=None
    alu_comuna_fam: Optional[str]=None
    alu_fono_fam: Optional[str]=None
    alu_e_mail2: Optional[str]=None
    alu_celular: Optional[str]=None
    aca_rut: Optional[str]=None

    class Config:
        orm_mode = True
    
class RequestAlumno_car(BaseModel):
    parameter: Alumno_carSchema = Field(...)

#NEW
class AsignaturaSchema(BaseModel):
    asi_cod: Optional[int] = None
    asi_nom: Optional[str] = None
    asi_teo: Optional[int] = None
    asi_ejer: Optional[int] = None
    asi_lab: Optional[int] = None

    class Config:
        orm_mode = True
    
class RequestAsignatura(BaseModel):
    parameter: AsignaturaSchema = Field(...)
    
#NEW
class ComunaSchema(BaseModel):
    com_cod: Optional[int] = None
    com_nom: Optional[str] = None
    com_reg_cod: Optional[int] = None
    com_cod_ofi: Optional[int] = None

    class Config:
        orm_mode = True
    
class RequestComuna(BaseModel):
    parameter: ComunaSchema = Field(...)

#NEW
class CursoSchema(BaseModel):
    cur_asign: Optional[int] = None
    cur_elect: Optional[str] = None
    cur_coord: Optional[str] = None
    cur_agno: Optional[int] = None
    cur_sem: Optional[int] = None

    class Config:
        orm_mode = True
    
class RequestCurso(BaseModel):
    parameter: CursoSchema = Field(...)