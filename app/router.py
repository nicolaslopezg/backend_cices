from urllib.request import Request
from fastapi import APIRouter, HTTPException, Path, Depends
from config import SessionLocal
from sqlalchemy.orm import Session
from schemas import BookSchema, RequestBook, Response, CategoriaSchema, RequestCategoria, Alumno_carSchema, RequestAlumno_car
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

@router.get("/categoria")
async def get(db:Session=Depends(get_db)):
    _categoria = crud.get_categoria(db,0,1000)
    return Response(code=200,status="Ok",message="Success Fetch all data",result=_categoria).dict(exclude_none=True)



@router.get("/alumno_car")
async def get(db:Session=Depends(get_db)):
    _alumno_car = crud.get_alumno_car(db,0,100)
    return Response(code=200,status="Ok",message="Success Fetch all data",result=_alumno_car).dict(exclude_none=True)