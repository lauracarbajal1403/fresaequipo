from fastapi import FastAPI, Form, HTTPException, Request, Path
from pydantic import BaseModel
from dbgrupos import dbgrupos
from dbalumnos import dbalumnos
from dbprofesores import dbprofesores
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from conexion import conexion
from dbmodulos import dbmodulos
import os
from dbcalificaciones import dbcalificaciones
from typing import List, Optional
from fastapi import Body, Query
db_calif = dbcalificaciones()
# ==============================
# INSTANCIAR LA APLICACIÓN FASTAPI
# ==============================
# Punto de entrada del backend. Aquí se configuran middlewares, rutas y modelos.
app = FastAPI()

# ==============================
# INSTANCIAS DE CAPA DE DATOS
# ==============================
# Cada clase (db_*) encapsula operaciones CRUD hacia PostgreSQL.
db_modulos = dbmodulos()
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
current_dir = os.path.dirname(os.path.abspath(__file__)) # ruta base del proyecto
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
    return HTMLResponse(home)

@app.get("/modulos", response_class=HTMLResponse)
def read_modulos():
    """
    Renderiza modulos.html con header y footer.
    """
    modulos_file = os.path.join(current_dir, "..", "front", "modulos.html")
    with open(modulos_file, "r", encoding="utf-8") as f1:
        modulos = f1.read()
    return HTMLResponse(modulos)

@app.get("/sesion", response_class=HTMLResponse)
def read_sesion():
   
    home_file = os.path.join(current_dir, "..", "front", "index.html")
    with open(home_file, "r", encoding="utf-8") as f1:
        home = f1.read()
    return HTMLResponse(home)

@app.get("/grupos", response_class=HTMLResponse)
def read_grupos():
    """
    Renderiza grupos.html con header y footer.
    """
    grupos_file = os.path.join(current_dir, "..", "front", "grupos.html")
    with open(grupos_file, "r", encoding="utf-8") as f1:
        grupos = f1.read()
   
    return HTMLResponse(grupos)

@app.get("/crudgrupos", response_class=HTMLResponse)
def read_crudgrupos():
    """
    Vista CRUD de grupos (frontend estático + header/footer).
    """
    grupos_file = os.path.join(current_dir, "..", "front", "crudgrupos.html")
    with open(grupos_file, "r", encoding="utf-8") as f1:
        grupos = f1.read()
    
    
    return HTMLResponse(grupos)

@app.get("/profes", response_class=HTMLResponse)
def read_profesores():
    """
    Renderiza profes.html con header y footer.
    """
    home_file = os.path.join(current_dir, "..", "front", "profes.html")
    with open(home_file, "r", encoding="utf-8") as f1:
        home1 = f1.read()
    
    return HTMLResponse(home1)

@app.get("/crudprofe", response_class=HTMLResponse)
def read_crudprofe():
    """
    Vista CRUD de profesores con header y footer.
    """
    home_file = os.path.join(current_dir, "..", "front", "crudprofe.html")
    with open(home_file, "r", encoding="utf-8") as f1:
        home1 = f1.read()

    return HTMLResponse(home1)

@app.get("/alumnos", response_class=HTMLResponse)
def read_alumnos():
    """
    Renderiza alumnos.html con header y footer.
    """
    alumnos_file = os.path.join(current_dir, "..", "front", "alumnos.html")
    with open(alumnos_file, "r", encoding="utf-8") as f1:
        alumnos = f1.read()
    return HTMLResponse(alumnos)

@app.get("/crudalumnos", response_class=HTMLResponse)
def read_crudalumnos():
    """
    Vista CRUD de alumnos con header y footer.
    """
    alumnos_file = os.path.join(current_dir, "..", "front", "crudalumnos.html")
    with open(alumnos_file, "r", encoding="utf-8") as f1:
        alumnos = f1.read()
    return HTMLResponse(alumnos)

@app.get("/crudmodulos", response_class=HTMLResponse)
def read_crudmodulos(): 
    """
    Vista CRUD de módulos con header y footer.
    """
    modulos_file = os.path.join(current_dir, "..", "front", "crudmodulos.html")
    with open(modulos_file, "r", encoding="utf-8") as f1:
        modulos = f1.read()
    return HTMLResponse(modulos)
# ==============================
# MODELOS (Pydantic)
# ==============================
# Definen la forma de los datos que entran/salen en endpoints.
class loginData(BaseModel):
    id: int
    contrasenia: str

class Grupo(BaseModel):
    codigo: int
    horario: str

class Alumno(BaseModel):
    codigo: int
    nombre: str
    horario: str
    codpro: int
    nomina: int
    estado: str

class Profesor(BaseModel):
    perfil: str
    nombre: str
    horario: str
    contrasenia: str
    contacto: int

class Modulo(BaseModel):
    nivel: str
    detalles: str
    libros: int
class CalificacionIn(BaseModel):
    modulo_nivel: str
    calificacion: Optional[float] = None
    observaciones: Optional[str] = None
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
@app.get("/alumnosobtener")
def get_alumnos():
    """
    Lista todos los alumnos (devuelve arreglo de objetos).
    - Fuente: db_alumnos.listar_alumnos().
 """
    try:
        con = conexion()
        conn = con.open()
        cursor = conn.cursor()

        sql = "SELECT id, nombre, nomina, profesor_id, horario, estado FROM alumnos ORDER BY id DESC"
        cursor.execute(sql)
        rows = cursor.fetchall()

        alumnos = []
        for r in rows:
            alumnos.append({
                "codigo": r[0],
                    "nombre": r[1],
                    "nomina": r[2],
                    "codpro": r[3],
                    "horario": r[4],
                    "estado": r[5],
            })
            
        return  {"alumnos": alumnos}
    except Exception as e:
            return {"error": str(e)}
    finally:
            try:
                cursor.close()
                conn.close()
            except Exception:
                pass
@app.get("/alumnos/{alumno_id}/calificaciones")
def get_calificaciones(alumno_id: int):
    rows = db_calif.obtener_por_alumno(alumno_id)
    promedio = db_calif.promedio_alumno(alumno_id)
    return {"calificaciones": rows, "promedio": promedio}

@app.post("/alumnos/{alumno_id}/calificaciones")
def upsert_calificaciones(alumno_id: int, payload: List[CalificacionIn]):
    ok = db_calif.upsert_lista(alumno_id, [p.model_dump() for p in payload])
    return {"ok": ok}
@app.get("/buscaralumno/{nombre}")
def get_alumno(nombre: str = None):
    try:
        print(f"Parametro recibido: {nombre}")

        if not nombre:
            return {"alumnos": []}

        alumnos = db_alumnos.buscar_alumno(nombre)
        return {"alumnos": alumnos or []}

    except Exception as e:
        print(f"Error en endpoint buscar: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/buscarestado")
def estado_alumno(estado: str = Query(...)):
    """
    Verifica si un alumno existe por su estado.
    """
    alumno = db_alumnos.buscar_estado(estado)
    return alumno
@app.get("/buscarinactivo")
def inactivo_alumno(estado: str = Path(...)):
    """
    Verifica si un alumno existe por su estado.
    """
    alumno = db_alumnos.buscar_inactivo(estado)
    return alumno
@app.api_route("/nuevo_alumno", methods=["POST", "GET"])
def agregar_alumno(
    nombre: str = Form(...),
    codigo: int = Form(...),
    horario: str = Form(...),
    codpro: int = Form(...),
    nomina: int = Form(...),
    estado: str = Form(...),
):
    """
    Crea un alumno. (Nota: Form(...) requiere método POST en uso real del navegador).
    - Recibe: nombre, contrasena, contacto, perfil, horario por form-data.
    - Inserta vía db_alumnos.nuevo_alumno.
    """
    alumno = Alumno(
        codigo = codigo,
        nombre = nombre,
        horario = horario,
        codpro = codpro,
        nomina = nomina,
        estado = estado,
    )
    db_alumnos.nuevo_alumno(alumno)
    return {"mensaje": "Alumno agregado correctamente"}


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
@app.get("/buscargrupos")
def buscar_grupos(gr : Grupo):
    """
    Lista todos los grupos registrados (id, horario).
    - Fuente: db_grupos.listar_grupos().
    """
    grupos = db_grupos.buscar_grupo(gr)
    return {"grupos": grupos}
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

# ==============================
# ENDPOINTS: Modulos
# ==============================
@app.api_route("/nuevo_modulo", methods=["POST", "GET"])
def nuevo_modulo(
    nivel: str = Form(...),
    libros: int = Form(...),
    detalles: str = Form(...),
    
):
    """
    Crea un nuevo módulo (campos: nivel, detalles, libros).
    - Recibe: 'nivel', 'detalles', 'libros' via form-data.
    - Llama a capa de datos (db_modulos.nuevo_modulo).
    """
    modulo = Modulo(
        nivel=nivel,
        libros=libros,
        detalles=detalles, 
    )
    db_modulos.nuevo_modulo(modulo)
    return {"mensaje": "Módulo agregado correctamente"}
@app.get("/modulosobtener")
def get_modulos():
    """
    Lista todos los módulos (devuelve arreglo de objetos).
    - Fuente: db_modulos.listar_modulos().
 """
    try:
        con = conexion()
        conn = con.open()
        cursor = conn.cursor()

        sql = "SELECT nivel, detalles, libros FROM modulos ORDER BY nivel DESC"
        cursor.execute(sql)
        rows = cursor.fetchall()

        modulos = []
        for r in rows:
            modulos.append({
                "nivel": r[0],
                    "detalles": r[1],
                    "libros": r[2],
            })
            
        return  {"modulos": modulos}
    except Exception as e:
            return {"error": str(e)}
    finally:
            try:
                cursor.close()
                conn.close()
            except Exception:
                pass    
@app.get("/buscarmodulo")
def get_modulo(nivel: str = Path(...)):
    """
    Obtiene un módulo por su nivel.
    - Retorna objeto con datos del módulo.
    """
    modulo = db_modulos.buscar_modulo(nivel)
    return modulo   
@app.post("/editar_modulo/{nivel}")
def editar_modulo(
    nivel: str,
    detalles: str = Form(...),
    libros: int | None = Form(None),
):
    """
    Actualiza un módulo existente (identificado por 'nivel').
    - Recibe campos por form-data y delega edición a db_modulos.editar_modulo.
    """
    class M: pass
    m = M()
    m.nivel = nivel
    m.detalles = detalles
    m.libros = libros
    db_modulos.editar_modulo(m)
    return {"mensaje": "Módulo actualizado"}
@app.delete("/eliminar_modulo/{nivel}")
def eliminar_modulo(nivel: str):
    """
    Elimina un módulo por 'nivel'.
    """
    db_modulos.eliminar_modulo(nivel)
    return {"mensaje": "Módulo eliminado"}