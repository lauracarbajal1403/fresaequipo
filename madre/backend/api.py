# ==============================
# IMPORTACIÓN DE LIBRERÍAS
# ==============================
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

# ==============================
# INSTANCIAR LA APLICACIÓN FASTAPI
# ==============================
# Punto de entrada del backend. Aquí se configuran middlewares, rutas y modelos.
app = FastAPI()

# ==============================
# INSTANCIAS DE CAPA DE DATOS
# ==============================
# Cada clase (db_*) encapsula operaciones CRUD hacia PostgreSQL.
db_grupos = dbgrupos()
db_alumnos = dbalumnos()
db_profesores = dbprofesores()

# ==============================
# CORS
# ==============================
# Define qué orígenes (frontends) pueden consumir este backend.
# IMPORTANTE: agregar aquí otros dominios/puertos del front si corresponde.
origins = [
    "https://fresaequipo-1.onrender.com",  # front en producción
    "http://localhost:8000",                # front local para pruebas
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,   # restringe a los orígenes listados
    allow_credentials=True,
    allow_methods=["*"],     # permite todos los métodos HTTP
    allow_headers=["*"],     # permite todos los headers
)

# ==============================
# ARCHIVOS ESTÁTICOS
# ==============================
# Sirve el front (HTML/CSS/JS) desde /front sin pasar por plantillas.
current_dir = os.path.dirname(os.path.abspath(__file__)) # carpeta /back
front_dir = os.path.join(current_dir, "..", "front")     # carpeta del front
app.mount("/front", StaticFiles(directory=front_dir), name="front")

# ==============================
# RUTAS DE PÁGINAS (HTML puro)
# ==============================
# Nota: Estas rutas devuelven HTML ya armado desde archivos del front.

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    """
    Página principal. Entrega el index.html del front.
    """
    index_path = os.path.join(front_dir, "index.html")
    with open(index_path, encoding="utf-8") as f:
        return HTMLResponse(f.read())

@app.get("/home", response_class=HTMLResponse)
def read_home():
    """
    Renderiza home.html rodeado por parte1.html (header) y parte2.html (footer).
    """
    home_file = os.path.join(current_dir, "..", "front", "home.html")
    with open(home_file, "r", encoding="utf-8") as f1:
        home = f1.read()
    part1 = os.path.join(current_dir, "..", "front", "parte1.html")
    part2 = os.path.join(current_dir, "..", "front", "parte2.html")
    with open(part1, "r", encoding="utf-8") as f2:
        part1 = f2.read()
    with open(part2, "r", encoding="utf-8") as f3:
        part2 = f3.read()
    full_html = part1 + home + part2
    return HTMLResponse(full_html)

@app.get("/grupos", response_class=HTMLResponse)
def read_grupos():
    """
    Renderiza grupos.html con header y footer.
    """
    grupos_file = os.path.join(current_dir, "..", "front", "grupos.html")
    with open(grupos_file, "r", encoding="utf-8") as f1:
        grupos = f1.read()
    part1 = os.path.join(current_dir, "..", "front", "parte1.html")
    part2 = os.path.join(current_dir, "..", "front", "parte2.html")
    with open(part1, "r", encoding="utf-8") as f2:
        part1 = f2.read()
    with open(part2, "r", encoding="utf-8") as f3:
        part2 = f3.read()
    full_html = part1 + grupos + part2
    return HTMLResponse(full_html)

@app.get("/crudgrupos", response_class=HTMLResponse)
def read_crudgrupos():
    """
    Vista CRUD de grupos (frontend estático + header/footer).
    """
    grupos_file = os.path.join(current_dir, "..", "front", "crudgrupos.html")
    with open(grupos_file, "r", encoding="utf-8") as f1:
        grupos = f1.read()
    part1 = os.path.join(current_dir, "..", "front", "parte1.html")
    part2 = os.path.join(current_dir, "..", "front", "parte2.html")
    with open(part1, "r", encoding="utf-8") as f2:
        part1 = f2.read()
    with open(part2, "r", encoding="utf-8") as f3:
        part2 = f3.read()
    full_html = part1 + grupos + part2
    return HTMLResponse(full_html)

@app.get("/profes", response_class=HTMLResponse)
def read_profesores():
    """
    Renderiza profes.html con header y footer.
    """
    home_file = os.path.join(current_dir, "..", "front", "profes.html")
    with open(home_file, "r", encoding="utf-8") as f1:
        home1 = f1.read()
    part1 = os.path.join(current_dir, "..", "front", "parte1.html")
    part2 = os.path.join(current_dir, "..", "front", "parte2.html")
    with open(part1, "r", encoding="utf-8") as f2:
        part1 = f2.read()
    with open(part2, "r", encoding="utf-8") as f3:
        part2 = f3.read()
    full_html = part1 + home1 + part2
    return HTMLResponse(full_html)

@app.get("/crudprofe", response_class=HTMLResponse)
def read_crudprofe():
    """
    Vista CRUD de profesores con header y footer.
    """
    home_file = os.path.join(current_dir, "..", "front", "crudprofe.html")
    with open(home_file, "r", encoding="utf-8") as f1:
        home1 = f1.read()
    part1 = os.path.join(current_dir, "..", "front", "parte1.html")
    part2 = os.path.join(current_dir, "..", "front", "parte2.html")
    with open(part1, "r", encoding="utf-8") as f2:
        part1 = f2.read()
    with open(part2, "r", encoding="utf-8") as f3:
        part2 = f3.read()
    full_html = part1 + home1 + part2
    return HTMLResponse(full_html)

# ==============================
# MODELOS (Pydantic)
# ==============================
# Definen la forma de los datos que entran/salen en endpoints.
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

# ==============================
# ENDPOINTS: GRUPOS
# ==============================
@app.post("/nuevo_grupo")
def agregar_grupo(horario: str = Form(...)):
    """
    Crea un nuevo grupo (campo mínimo: horario).
    - Recibe: 'horario' via form-data.
    - Llama a capa de datos (db_grupos.nuevo_grupo).
    """
    grupo = Grupo(horario=horario)
    db_grupos.nuevo_grupo(grupo)
    return {"mensaje": "Grupo agregado correctamente"}

# ==============================
# ENDPOINTS: ALUMNOS
# ==============================
@app.get("/alumnos")
def get_alumnos():
    """
    Lista todos los alumnos (devuelve arreglo de objetos).
    - Fuente: db_alumnos.listar_alumnos().
    """
    return db_alumnos.listar_alumnos()

@app.post("/nuevo_alumno")
def nuevo_alumno(
    nombre: str = Form(...),
    horario: str = Form(...),
    nomina: int | None = Form(None),
    codpro: int | None = Form(None),
):
    """
    Crea un alumno con datos mínimos (nombre, horario) y opcionales (nomina, codpro).
    - Genera un objeto temporal con los atributos esperados por db_alumnos.nuevo_alumno.
    - Retorna mensaje de confirmación y el código asignado (si lo gestiona la capa de datos).
    """
    class A: pass
    a = A()
    a.nombre = nombre
    a.horario = horario
    a.nomina = nomina
    a.codpro = codpro # Representa el código del profesor (por ejemplo, el ID del profesor que 
                      # imparte el grupo o está asignado al alumno)."""

    new_id = db_alumnos.nuevo_alumno(a)
    return {"mensaje": "Alumno creado", "codigo": new_id}

@app.post("/editar_alumno/{codigo}")
def editar_alumno(
    codigo: int,
    nombre: str = Form(...),
    horario: str = Form(...),
    nomina: int | None = Form(None),
    codpro: int | None = Form(None),
):
    """
    Actualiza un alumno existente (identificado por 'codigo').
    - Recibe campos por form-data y delega edición a db_alumnos.editar_alumno.
    """
    class A: pass
    a = A()
    a.codigo = codigo
    a.nombre = nombre
    a.horario = horario
    a.nomina = nomina
    a.codpro = codpro
    db_alumnos.editar_alumno(a)
    return {"mensaje": "Alumno actualizado"}

@app.delete("/eliminar_alumno/{codigo}")
def eliminar_alumno(codigo: int):
    """
    Elimina un alumno por 'codigo'.
    """
    db_alumnos.eliminar_alumno(codigo)
    return {"mensaje": "Alumno eliminado"}

# ==============================
# ENDPOINTS: PROFESORES
# ==============================
@app.api_route("/eliminar_profesor/{id}", methods=["DELETE"])
def eliminar_profesor(id: int = Path(...)):
    """
    Elimina un profesor por ID.
    """
    db_profesores.eliminar_profesor(id)
    return {"mensaje": "Profesor eliminado correctamente"}

@app.api_route("/nuevo_profesor", methods=["POST", "GET"])
def agregar_profesor(
    nombre: str = Form(...),
    contrasenia: str = Form(...),
    contacto: str = Form(...),
    perfil: str = Form(...),
    horario: str = Form(...),
):
    """
    Crea un profesor. (Nota: Form(...) requiere método POST en uso real del navegador).
    - Recibe: nombre, contrasenia, contacto, perfil, horario por form-data.
    - Inserta vía db_profesores.nuevo_profesor.
    """
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
    """
    Autenticación básica de profesor.
    - Recibe JSON: { id, contrasenia }.
    - Respuesta: mensaje + datos del profesor si es válido.
    """
    resultado = db_profesores.autentificar(profe)
    if resultado:
        return {"mensaje": "Profesor autenticado correctamente", "profesor": resultado}
    else:
        return {"mensaje": "Error de autenticación"}

@app.get("/profesores")
def obtener_profesores():
    """
    Devuelve listado de profesores (consulta directa con 'conexion').
    - Retorna: {profesores: [ {id, nombre, perfil, horario, contacto}, ... ]}
    """
    try:
        conx = conexion()
        conn = conx.open()
        cursor = conn.cursor()
        cursor.execute(
            "SELECT id, nombre, perfil, horario, contacto FROM profesores ORDER BY id;"
        )
        filas = cursor.fetchall()
        profesores = []
        for fila in filas:
            profesores.append({
                "id": fila[0],
                "nombre": fila[1],
                "perfil": fila[2],
                "horario": fila[3],
                "contacto": fila[4],
            })
        return {"profesores": profesores}
    except Exception as e:
        return {"error": str(e)}
    finally:
        # Cierra recursos si fueron creados correctamente
        try:
            cursor.close()
            conn.close()
        except Exception:
            pass

# ==============================
# ENDPOINTS COMPLEMENTARIOS
# ==============================
@app.get("/horarios")
def get_horarios():
    """
    Lista los 'horarios' existentes en la tabla 'grupos'.
    - Útil para llenar combos/selects en el frontend.
    """
    conx = conexion()
    conn = conx.open()
    cursor = conn.cursor()
    cursor.execute("SELECT horario FROM grupos")
    horarios = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return {"horarios": horarios}

@app.get("/gruposver")
def obtener_gruposver():
    """
    Lista todos los grupos registrados (id, horario).
    """
    try:
        conx = conexion()
        conn = conx.open()
        cursor = conn.cursor()
        cursor.execute("SELECT id, horario, contacto FROM grupos ORDER BY id;")
        filas = cursor.fetchall()
        grupos = []
        for fila in filas:
            grupos.append({
                "id": fila[0],
                "horario": fila[1],
            })
        return {"grupos": grupos}
    except Exception as e:
        return {"error": str(e)}
    finally:
        try:
            cursor.close()
            conn.close()
        except Exception:
            pass
