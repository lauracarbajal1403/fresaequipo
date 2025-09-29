import psycopg2
import conexion as con 
class dbalumnos:
    def nuevo_alumno(self, alumno):        
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "INSERT INTO alumnos (codigo, nomina, nombre, codpro, grupo) VALUES ( %s, %s, %s, %s, %s)"
            self.datos = (
                alumno.codigo,
                alumno.nomina, 
                alumno.nombre,
                alumno.codpro,
                alumno.horario
            )
            self.cursor.execute(self.sql, self.datos)
            self.conn.commit()
        except psycopg2.Error as e:
            print(f"Error al guardar alumno: {e}")
        finally:
            self.conn.close()
    """
    def buscar_alumno(self, alumno):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1=self.conn.cursor()
            auxi=None
            self.sql = "SELECT * FROM alumnos WHERE codigo = %s"
            self.cursor1.execute(self.sql, (alumno.codigo(),))
            row = self.cursor1.fetchone()
            self.conn.commit()
            self.conn.close()
            print("wow")
            if row[2] is not None:
                print("ok")
                auxi = al.alumnos()
                auxi.setcodigo(row[0])
                auxi.setnomina(row[1])
                auxi.setnombre(row[2])
                auxi.setcodpro(row[3])
                auxi.setgrupo(row[4])
        except Exception as e:
            print(f"Error al buscar alumno: {e}")
            return None
        return auxi
    """   
    def editar_alumno(self, alumno):
        self.con=con.conexion()
        self.conn=self.con.open()
        self.cursor1=self.conn.cursor()
        self.sql="update alumnos set nomina=%s,codpro=%s, grupo=%s where codigo={}".format(alumno.getcodigo())
        self.datos=(alumno.nomina,
                    alumno.codpro,
                    alumno.grupo)
        self.cursor1.execute(self.sql, self.datos)
        self.conn.commit()
        self.conn.close()
    
    def eliminar_alumno(self, alumno):
        self.con=con.conexion()
        self.conn=self.con.open()
        self.cursor1=self.conn.cursor()
        self.sql = "DELETE FROM alumnos WHERE codigo = %s"
        self.cursor1.execute(self.sql, (alumno.codigo(),))
        self.conn.commit()

    def getid_alumno(self):
        id=1
        self.con=con.conexion()
        self.conn=self.con.open()
        self.cursor=self.conn.cursor()
        self.sql="select max(codigo) as id from alumnos"
        self.cursor.execute(self.sql)
        row=self.cursor.fetchone()
        self.cursor.close()
        self.conn.close()
        if row[0] is None:
            return 1
        else:
            return row[0] + 1