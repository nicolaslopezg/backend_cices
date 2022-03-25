from sqlalchemy.orm import Session
from model import *
from schemas import *

def get_book(db:Session,skip:int=0,limit:int=100):
    return db.query(Book).offset(skip).limit(limit).all()

# def get_book_by_id(db:Session,book_id:int):
#     return db.query(Book).filter(Book.id == book_id).first()

# def create_book(db:Session, book: BookSchema):
#     _book = Book(title=book.title,description=book.description)
#     db.add(_book)
#     db.commit()
#     db.refresh(_book)
#     return _book

# def remove_book(db:Session,book_id:int):
#     _book = get_book_by_id(db=db,book_id=book_id)
#     db.delete(_book)
#     db.commit()

# def update_book(db:Session,book_id:int,title:str,description:str):
#     _book = get_book_by_id(db=db,book_id=book_id)
#     _book.title = title
#     _book.description = description
#     db.commit()
#     db.refresh(_book)
#     return _book


def get_categoria(db:Session,skip:int=0,limit:int=100):
    return db.query(Categoria).offset(skip).limit(limit).all()



def get_alumno_car(db:Session,skip:int=0,limit:int=100):
    return db.query(Alumno_car).offset(skip).limit(limit).all()


def get_asignatura(db:Session,skip:int=0,limit:int=100):
    return db.query(Asignatura).offset(skip).limit(limit).all()

    
def get_comuna(db:Session,skip:int=0,limit:int=100):
    return db.query(Comuna).offset(skip).limit(limit).all()

    
def get_curso(db:Session,skip:int=0,limit:int=100):
    return db.query(Curso).offset(skip).limit(limit).all()