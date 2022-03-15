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