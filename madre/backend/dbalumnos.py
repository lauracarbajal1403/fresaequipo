# =======================================================
# MÓDULO: dbalumnos.py
# DESCRIPCIÓN:
#   Clase que gestiona las operaciones CRUD (Crear, Leer,
#   Actualizar, Eliminar) sobre la tabla 'alumnos' en la base de datos PostgreSQL.
#   Utiliza el módulo de conexión 'conexion.py' para establecer la comunicación.
# =======================================================

import psycopg2           # Librería para conectarse y ejecutar consultas en PostgreSQL
import conexion as con     # Módulo personalizado que gestiona la conexión a la base de datos
import datetime

class dbalumnos:
    """
    Clase dbalumnos:
    Encapsula todas las operaciones relacionadas con la tabla 'alumnos'.
    Cada método abre su propia conexión, ejecuta la acción y la cierra.
    """

    # ---------------------------------------------------
    # MÉTODO: nuevo_alumno
    # DESCRIPCIÓN: Inserta un nuevo registro de alumno en la base de datos.
    # PARÁMETRO: alumno -> objeto que contiene los atributos del alumno.
    # ---------------------------------------------------
    def nuevo_alumno(self, alumno):
        try:
            # Establece la conexión con la base de datos
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()

            # Sentencia SQL para insertar datos en la tabla
            self.sql = "INSERT INTO alumnos (id, nomina, nombre, profesor_id, horario, estado) VALUES ( %s, %s, %s, %s, %s, %s)"

            # Tupla con los datos que se insertarán
            self.datos = (
                alumno.codigo,
                alumno.nomina,
                alumno.nombre,
                alumno.codpro,
                alumno.horario,
                alumno.estado
            )

            # Ejecuta la consulta y guarda los cambios
            self.cursor.execute(self.sql, self.datos)
            self.conn.commit()

        except psycopg2.Error as e:
            # Captura y muestra errores de PostgreSQL
            print(f"Error al guardar alumno: {e}")

        finally:
            # Cierra la conexión a la base de datos
            self.conn.close()


    # ---------------------------------------------------
    # MÉTODO: editar_alumno
    # DESCRIPCIÓN: Actualiza los datos de un alumno existente.
    # ---------------------------------------------------
    def editar_alumno(self, alumno):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()

            # Sentencia SQL para actualizar campos del alumno
            sql = "UPDATE alumnos SET nombre=%s, nomina=%s, profesor_id=%s, horario=%s WHERE id=%s"
            datos = (alumno.nombre, alumno.nomina, alumno.codpro, alumno.horario, alumno.codigo)

            self.cursor.execute(sql, datos)
            self.conn.commit()

        except psycopg2.Error as e:
            print(f"Error al editar alumno: {e}")
            raise  # Relanza la excepción si se requiere manejar más arriba

        finally:
            # Cierra recursos de manera segura
            try:
                self.cursor.close()
                self.conn.close()
            except Exception:
                pass


    # ---------------------------------------------------
    # MÉTODO: eliminar_alumno
    # DESCRIPCIÓN: Elimina un registro de alumno usando su código.
    # ---------------------------------------------------
    def eliminar_alumno(self, codigo):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()

            sql = "DELETE FROM alumnos WHERE id=%s"
            self.cursor.execute(sql, (codigo,))
            self.conn.commit()

        except psycopg2.Error as e:
            print(f"Error al eliminar alumno: {e}")
            raise

        finally:
            try:
                self.cursor.close()
                self.conn.close()
            except Exception:
                pass


    # ---------------------------------------------------
    # MÉTODO: getid_alumno
    # DESCRIPCIÓN: Obtiene el siguiente ID disponible para insertar un nuevo alumno.
    # RETORNA: entero (el siguiente código disponible).
    # ---------------------------------------------------
    def getid_alumno(self):
        id = 1
        self.con = con.conexion()
        self.conn = self.con.open()
        self.cursor = self.conn.cursor()

        # Consulta el último código insertado
        self.sql = "SELECT max(id) as id FROM alumnos"
        self.cursor.execute(self.sql)
        row = self.cursor.fetchone()

        self.cursor.close()
        self.conn.close()

        # Si no hay registros, devuelve 1; de lo contrario, incrementa el último ID
        if row[0] is None:
            return 1
        else:
            return row[0] + 1
    # ---------------------------------------------------
    # MÉTODO: buscar_alumno
    # DESCRIPCIÓN: Busca un alumno por su nombre.
    # RETORNA: objeto alumno o None si no se encuentra.
    # ---------------------------------------------------

    def buscar_alumno(self, nombre_buscar):
        """
        Busca alumnos por nombre (búsqueda parcial con LIKE)
        """
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1 = self.conn.cursor()
            
            # Usar LIKE para búsqueda parcial (encuentra "Laura" si buscas "la")
            self.sql = "SELECT * FROM alumnos WHERE nombre LIKE %s"
            self.cursor1.execute(self.sql, (f"%{nombre_buscar}%",))
            rows = self.cursor1.fetchall()
            
            self.conn.close()
            
            # Convertir las filas a lista de diccionarios
            alumnos = []
            for row in rows:
                alumno = {
                    "codigo": row[0],
                    "nombre": row[1],
                    "nomina": row[2],
                    "codpro": row[3],
                    "horario": row[4],
                    "estado": row[5]
                }
                alumnos.append(alumno)
            
            return alumnos
            
        except Exception as e:
            print(f"Error al buscar alumno: {e}")
            if self.conn:
                self.conn.close()
            return []
    # ---------------------------------------------------
    # MÉTODO: buscar_alumno
    # DESCRIPCIÓN: Busca un alumno por su estado.
    # RETORNA: objeto alumno o None si no se encuentra.
    # ---------------------------------------------------
    def buscar_estado(self, alumno):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1=self.conn.cursor()
            auxi=None
            self.sql = "SELECT * FROM alumnos WHERE estado = 'activo'"
            self.cursor1.execute(self.sql, (alumno.estado,))
            row = self.cursor1.fetchone()
            
            self.conn.commit()
            return row
        except Exception as e:
            print(f"Error al buscar alumno: {e}")
            if self.conn:
                self.conn.close()
            return None

    def mensualidades(self, alumno):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1=self.conn.cursor()
            auxi=None
            self.sql = "SELECT * FROM alumnos WHERE mensualidades = %s"
            self.cursor1.execute(self.sql, (alumno.mensualidades,))
            row = self.cursor1.fetchone()
            self.conn.commit()
            self.conn.close()
            print("wow")
            if row[1] is not None:
                print("ok")
                alumno.setid(row[0])
                alumno.setnombre(row[1])
                alumno.setnomina(row[2])
                alumno.setcodpro(row[3])
                alumno.sethorario(row[4])
        except Exception as e:
            print(f"Error al buscar alumno: {e}")
            return None
        return alumno 
