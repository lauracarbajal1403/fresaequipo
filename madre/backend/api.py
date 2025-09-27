from fastapi import FastAPI, Request
from pydantic import BaseModel
from dbgrupos import dbgrupos
from dbalumnos import dbalumnos 
from dbprofesores import dbprofesores
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import os
app = FastAPI()
db_grupos = dbgrupos()
db_alumnos = dbalumnos()
db_profesores = dbprofesores()
origins =[
    "https://fresaequipo-1.onrender.com",
    "http://localhost:8000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
current_dir = os.path.dirname(os.path.abspath(__file__))
front_dir = os.path.join(current_dir, "..", "front")
app.mount("/front", StaticFiles(directory=front_dir), name="front")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    index_path = os.path.join(front_dir, "index.html")  
    with open(index_path, encoding="utf-8") as f:
        return HTMLResponse(f.read())


@app.get("/home", response_class=HTMLResponse)
def read_home():
    home_file = os.path.join(current_dir, "..", "front", "home.html")
    with open(home_file, "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())
@app.get("/parte1", response_class=HTMLResponse)
def read_part1():
    part1 = os.path.join(current_dir, "..", "front",  "parte1.html")
    with open(part1, "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())
@app.get("/parte2", response_class=HTMLResponse)
def read_part2():
    part2 = os.path.join(current_dir,  "..", "front", "parte2.html")
    with open(part2, "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())

class Grupo(BaseModel):
    id: int
    grupo: str

class Alumno(BaseModel):
    codigo: int
    nombre: str
    horario: str
    codpro: int
    nomina: int
class Profesor(BaseModel):
    id: int
    nombre: str
    horario: str
    contrasenia: str
    contacto: str
    perfil: str


@app.post("/nuevo_grupo")
def agregar_grupo(grupo: Grupo):
    db_grupos.nuevo_grupo(grupo)
    return {"mensaje": "Grupo agregado correctamente"}

@app.post("/nuevo_alumno")
def agregar_alumno(alumno: Alumno):
    db_alumnos.nuevo_alumno(alumno)
    return {"mensaje": "Alumno agregado correctamente"}

@app.post("/nuevo_profesor")
def agregar_profesor(profe: Profesor):
    db_profesores.nuevo_profesor(profe)
    return {"mensaje": "Profesor agregado correctamente"}
@app.put("/verificar_profesor")
def verificar_profesor(profe: Profesor):
    resultado = db_profesores.autentificar(profe)
    if resultado:
        return {"mensaje": "Profesor autenticado correctamente", "profesor": resultado}
    else:
        return {"mensaje": "Error de autenticación"}