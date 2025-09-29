from fastapi import FastAPI, Form, Request, Path
from pydantic import BaseModel
from dbgrupos import dbgrupos
from dbalumnos import dbalumnos 
from dbprofesores import dbprofesores
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from conexion import conexion
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
    with open(home_file, "r", encoding="utf-8") as f1:
        home = f1.read()
    part1 = os.path.join(current_dir, "..", "front",  "parte1.html")
    part2 = os.path.join(current_dir,  "..", "front", "parte2.html")
    with open(part1, "r", encoding="utf-8") as f2:
        part1 = f2.read()
    with open(part2, "r", encoding="utf-8") as f3:
        part2 = f3.read()
    full_html = part1 + home + part2
    return HTMLResponse(full_html)

@app.get("/grupos", response_class=HTMLResponse)
def read_grupos():
    grupos_file = os.path.join(current_dir, "..", "front", "grupos.html")
    with open(grupos_file, "r", encoding="utf-8") as f1:
        grupos = f1.read()
    part1 = os.path.join(current_dir, "..", "front",  "parte1.html")
    part2 = os.path.join(current_dir,  "..", "front", "parte2.html")
    with open(part1, "r", encoding="utf-8") as f2:
        part1 = f2.read()
    with open(part2, "r", encoding="utf-8") as f3:
        part2 = f3.read()
    full_html = part1 + grupos + part2
    return HTMLResponse(full_html)


@app.get("/crudgrupos", response_class=HTMLResponse)
def read_crudgrupos():
    grupos_file = os.path.join(current_dir, "..", "front", "crudgrupos.html")
    with open(grupos_file, "r", encoding="utf-8") as f1:
        grupos = f1.read()
    part1 = os.path.join(current_dir, "..", "front",  "parte1.html")
    part2 = os.path.join(current_dir,  "..", "front", "parte2.html")
    with open(part1, "r", encoding="utf-8") as f2:
        part1 = f2.read()
    with open(part2, "r", encoding="utf-8") as f3:
        part2 = f3.read()
    full_html = part1 + grupos + part2
    return HTMLResponse(full_html)

@app.get("/profes", response_class=HTMLResponse)
def read_profesores():
    home_file = os.path.join(current_dir, "..", "front", "profes.html")
    with open(home_file, "r", encoding="utf-8") as f1:
        home1 = f1.read()
    part1 = os.path.join(current_dir, "..", "front",  "parte1.html")
    part2 = os.path.join(current_dir,  "..", "front", "parte2.html")
    with open(part1, "r", encoding="utf-8") as f2:
        part1 = f2.read()
    with open(part2, "r", encoding="utf-8") as f3:
        part2 = f3.read()
    full_html = part1 + home1 + part2
    return HTMLResponse(full_html)


@app.get("/crudprofe", response_class=HTMLResponse)
def read_crudprofe():
    home_file = os.path.join(current_dir, "..", "front", "crudprofe.html")
    with open(home_file, "r", encoding="utf-8") as f1:
        home1 = f1.read()
    part1 = os.path.join(current_dir, "..", "front",  "parte1.html")
    part2 = os.path.join(current_dir,  "..", "front", "parte2.html")
    with open(part1, "r", encoding="utf-8") as f2:
        part1 = f2.read()
    with open(part2, "r", encoding="utf-8") as f3:
        part2 = f3.read()
    full_html = part1 + home1 + part2
    return HTMLResponse(full_html)
class loginData(BaseModel):
    id: int
    contrasenia: str
class Grupo(BaseModel):
    horario: str

class Alumno(BaseModel):
    codigo: int
    nombre: str
    horario: str
    codpro: int
    nomina: int

class Profesor(BaseModel):
    perfil: str
    nombre: str
    horario: str
    contrasenia: str
    contacto: int
@app.post("/nuevo_grupo")
def agregar_grupo(horario: str = Form(...),):
    grupo = Grupo(
        horario=horario,
    )
    db_grupos.nuevo_grupo(grupo)
    return {"mensaje": "Grupo agregado correctamente"}

@app.post("/nuevo_alumno")
def agregar_alumno(alumno: Alumno):
    db_alumnos.nuevo_alumno(alumno)
    return {"mensaje": "Alumno agregado correctamente"}
@app.api_route("/eliminar_profesor/{id}", methods=["DELETE"])
def eliminar_profesor(id: int = Path(...)):
    db_profesores.eliminar_profesor(id)
    return {"mensaje": "Profesor eliminado correctamente"}
@app.api_route("/nuevo_profesor", methods=["POST", "GET"])
def agregar_profesor(
    nombre: str = Form(...),
    contrasenia: str = Form(...),
    contacto: str = Form(...),
    perfil: str = Form(...),
    horario: str = Form(...)
    ):
    profe = Profesor(
        nombre=nombre,
        contrasenia=contrasenia,
        contacto=contacto,
        perfil=perfil,
        horario=horario,
    )
    db_profesores.nuevo_profesor(profe)
    return {"mensaje": "Profesor agregado correctamente"}
@app.post("/login_profesor")
def verificar_profesor(profe: loginData):
    resultado = db_profesores.autentificar(profe)
    if resultado:
        return {"mensaje": "Profesor autenticado correctamente", "profesor": resultado}
    else:
        return {"mensaje": "Error de autenticación"}
@app.get("/profesores")
def obtener_profesores():
    try:
        con = conexion()
        conn = con.open()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, perfil, horario, contacto FROM profesores ORDER BY id;")
        filas = cursor.fetchall()
        profesores = []
        for fila in filas:
            profesores.append({
                "id": fila[0],
                "nombre": fila[1],
                "perfil": fila[2],
                "horario": fila[3],
                "contacto": fila[4]
            })
        return {"profesores": profesores}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()
@app.get("/horarios")
def get_horarios():
    con = conexion()
    conn = con.open()
    cursor = conn.cursor()
    cursor.execute("SELECT horario FROM grupos")
    horarios = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return {"horarios": horarios}
@app.get("/gruposver")
def obtener_gruposver():
    try:
        con = conexion()
        conn = con.open()
        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, perfil, horario, contacto FROM grupos ORDER BY id;")
        filas = cursor.fetchall()
        grupos = []
        for fila in filas:
            grupos.append({
                "id": fila[0],
                "horario": fila[1]
            })
        return {"grupos": grupos}
    except Exception as e:
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()