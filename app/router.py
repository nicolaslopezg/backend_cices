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

@router.get("/student")
async def get(db:Session=Depends(get_db)):
    _student = crud.get_student(db,0,1000)
    return Response(code=200,status="Ok",message="Success Fetch all data",result=_student).dict(exclude_none=True)

@router.get("/project")
async def get(db:Session=Depends(get_db)):
    _project = crud.get_project(db,0,1000)
    return Response(code=200,status="Ok",message="Success Fetch all data",result=_project).dict(exclude_none=True)

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

@router.get("/filter")
async def get(db:Session=Depends(get_db)):
    _filter = crud.get_filter(db,0,1000)
    return Response(code=200,status="Ok",message="Success Fetch all data",result=_filter).dict(exclude_none=True)