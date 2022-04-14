from urllib.request import Request
from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import *
import crud

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# @router.post('/create')
# async def create(request:RequestBook,db:Session=Depends(get_db)):
#     crud.create_book(db,book=request.parameter)
#     return Response(code=200,status="Ok",message="Book created successfully").dict(exclude_none=True)

# @router.get("/")
# async def get(db:Session=Depends(get_db)):
#     _book = crud.get_book(db,0,100)
#     return Response(code=200,status="Ok",message="Success Fetch all data",result=_book).dict(exclude_none=True)

# @router.get("/{id}")
# async def get_by_id(id:int, db:Session=Depends(get_db)):
#     _book = crud.get_book_by_id(db,id)
#     return Response(code=200,status="Ok",message="Success get data",result=_book).dict(exclude_none=True)

# @router.get("/update")
# async def update_book(request: RequestBook, db:Session=Depends(get_db)):
#     _book = crud.update_book(db,book_id=request.parameter.id,title=request.parameter.title, description=request.parameter.description)
#     return Response(code=200,status="Ok",message="Success update data",result=_book)

# @router.delete("/{id}")
# async def delete(id:int, db:Session=Depends(get_db)):
#     _book = crud.remove_book(db,book_id=id)
#     return Response(code=200,status="Ok",message="Success delete data",result=_book).dict(exclude_none=True)

# @router.get("/categoria")
# async def get(db:Session=Depends(get_db)):
#     _categoria = crud.get_categoria(db,0,1000)
#     return Response(code=200,status="Ok",message="Success Fetch all data",result=_categoria).dict(exclude_none=True)



# @router.get("/alumno_car")
# async def get(db:Session=Depends(get_db)):
#     _alumno_car = crud.get_alumno_car(db,0,100)
#     return Response(code=200,status="Ok",message="Success Fetch all data",result=_alumno_car).dict(exclude_none=True)

# @router.get("/asignatura")
# async def get(db:Session=Depends(get_db)):
#     _asignatura = crud.get_asignatura(db,0,1000)
#     return Response(code=200,status="Ok",message="Success Fetch all data",result=_asignatura).dict(exclude_none=True)

# @router.get("/comuna")
# async def get(db:Session=Depends(get_db)):
#     _comuna = crud.get_comuna(db,0,1000)
#     return Response(code=200,status="Ok",message="Success Fetch all data",result=_comuna).dict(exclude_none=True)

# @router.get("/curso")
# async def get(db:Session=Depends(get_db)):
#     _curso = crud.get_curso(db,0,1000)
#     return Response(code=200,status="Ok",message="Success Fetch all data",result=_curso).dict(exclude_none=True)

@router.get("/student")
async def get(db:Session=Depends(get_db)):
    _student = crud.get_student(db,0,1000)
    return Response(code=200,status="Ok",message="Success Fetch all data",result=_student).dict(exclude_none=True)

@router.get("/section")
async def get(db:Session=Depends(get_db)):
    _section = crud.get_section(db,0,1000)
    return Response(code=200,status="Ok",message="Success Fetch all data",result=_section).dict(exclude_none=True)

@router.get("/instructor")
async def get(db:Session=Depends(get_db)):
    _instructor = crud.get_instructor(db,0,1000)
    return Response(code=200,status="Ok",message="Success Fetch all data",result=_instructor).dict(exclude_none=True)

@router.get("/enrollment")
async def get(db:Session=Depends(get_db)):
    _enrollment = crud.get_enrollment(db,0,1000)
    return Response(code=200,status="Ok",message="Success Fetch all data",result=_enrollment).dict(exclude_none=True)

@router.get("/ed_center")
async def get(db:Session=Depends(get_db)):
    _ed_center = crud.get_ed_center(db,0,1000)
    return Response(code=200,status="Ok",message="Success Fetch all data",result=_ed_center).dict(exclude_none=True)

@router.get("/department")
async def get(db:Session=Depends(get_db)):
    _department = crud.get_department(db,0,1000)
    return Response(code=200,status="Ok",message="Success Fetch all data",result=_department).dict(exclude_none=True)

@router.get("/course")
async def get(db:Session=Depends(get_db)):
    _course = crud.get_course(db,0,1000)
    return Response(code=200,status="Ok",message="Success Fetch all data",result=_course).dict(exclude_none=True)