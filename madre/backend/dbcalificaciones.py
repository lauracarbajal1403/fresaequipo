# dbcalificaciones.py
import psycopg2
import psycopg2.extras
from conexion import conexion

class dbcalificaciones:
    def obtener_por_alumno(self, alumno_id: int):
        conx = conexion()
        conn = conx.open()
        cur  = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        try:
            sql = """
              SELECT c.alumno_id, c.modulo_nivel, c.calificacion, c.observaciones
                FROM calificaciones c
               WHERE c.alumno_id = %s
               ORDER BY c.modulo_nivel
            """
            cur.execute(sql, (alumno_id,))
            rows = cur.fetchall()
            return [dict(r) for r in rows]
        finally:
            cur.close(); conn.close()

    def upsert_lista(self, alumno_id: int, califs: list[dict]):
        """
        califs: [{modulo_nivel: str, calificacion: float|None, observaciones: str|None}, ...]
        Inserta/actualiza en bloque. Si calificacion es None => guarda NULL.
        """
        conx = conexion()
        conn = conx.open()
        cur  = conn.cursor()
        try:
            sql = """
              INSERT INTO calificaciones (alumno_id, modulo_nivel, calificacion, observaciones)
              VALUES (%s, %s, %s, %s)
              ON CONFLICT (alumno_id, modulo_nivel)
              DO UPDATE SET calificacion = EXCLUDED.calificacion,
                            observaciones = EXCLUDED.observaciones
            """
            datos = [
                (alumno_id, item["modulo_nivel"], item.get("calificacion"), item.get("observaciones"))
                for item in califs
            ]
            psycopg2.extras.execute_batch(cur, sql, datos, page_size=50)
            conn.commit()
            return True
        except Exception as e:
            conn.rollback()
            raise e
        finally:
            cur.close(); conn.close()

    def promedio_alumno(self, alumno_id: int) -> float | None:
        conx = conexion()
        conn = conx.open()
        cur  = conn.cursor()
        try:
            cur.execute("SELECT AVG(calificacion) FROM calificaciones WHERE alumno_id = %s", (alumno_id,))
            (avg,) = cur.fetchone()
            return float(avg) if avg is not None else None
        finally:
            cur.close(); conn.close()
