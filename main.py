from fastapi import FastAPI
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()

students = []

class Student(BaseModel):
    id: str
    nombre: str
    apellido: str

@app.get("/students")
def get_students():
    return students

@app.post("/students")
def save_students(student: Student):
    student.id = str(uuid4())
    students.append(student.dict())
    return "Estudiante registrado"

#GET estudiante en específico
@app.get("/students/{id}")
def get_student(id: str):
    for student in students:
        if student["id"] == id:
            return student
    return "No existe el estudiante"

@app.put("/students/{id}")
def update_student(update_student: Student, id: str):
    for student in students:
        if student["id"] == id:
            student["nombre"] = update_student.nombre
            student["apellido"] = update_student.apellido
            return "Estudiante actualizado"
    return "No existe el estudiante"

@app.delete("/students/{id}")
def update_student(id: str):
    for student in students:
        if student["id"] == id:
            students.remove(student)
    return "Estudiante eliminado"

@app.get("/")
def mensaje():
    return "Hola Mundo"

@app.get("/users/{user_id}")
def mensaje(user_id):
    return f"El id del user es: {user_id}"
