from fastapi import FastAPI, Request
from pydantic import BaseModel
from dbgrupos import dbgrupos
from dbalumnos import dbalumnos 
from dbprofesores import dbprofesores
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
app = FastAPI()
db_grupos = dbgrupos()
db_alumnos = dbalumnos()
db_profesores = dbprofesores()
origins =[
    "https://fresaequipo-1.onrender.com",
    "http://localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/public", StaticFiles(directory="public"), name="public")


@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    with open("public/index.html") as f:
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