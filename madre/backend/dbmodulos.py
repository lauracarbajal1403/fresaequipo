import conexion as con
import psycopg2

class dbmodulos:
    def nuevo_modulo(self, modulo):        
        conn = None
        try:
            self.con = con.conexion()
            conn = self.con.open()
            if conn is None:
                return
            cursor = conn.cursor()
            sql = "INSERT INTO modulos (nivel, detalles, libros) VALUES (%s, %s, %s)"
            datos = (modulo.nivel, modulo.detalles, modulo.libros)
            cursor.execute(sql, datos)
            conn.commit()
        except psycopg2.Error as e:
            print(f"Error al guardar modulo: {e}")
        finally:
            if conn:
                conn.close()


    def buscar_modulo(self, modulo):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1=self.conn.cursor()
            auxi=None
            self.sql = "SELECT * FROM modulos WHERE nivel = %s"
            self.cursor1.execute(self.sql, (modulo.getnivel(),))
            row = self.cursor1.fetchone()
            self.conn.commit()
            self.conn.close()
            print("wow")
            if row[0] is not None:
                print("ok")
                modulo.setnivel(row[0])
                modulo.setdetalles(row[1])
                modulo.setlibros(row[2])
        except Exception as e:
            print(f"Error al buscar modulo: {e}")
            return None
        return modulo

    def editar_modulo(self, modulo):
        self.con=con.conexion()
        self.conn=self.con.open()
        self.cursor1=self.conn.cursor()
        self.sql="update modulos set nivel=%s, detalles=%s, libros=%s where id=%s"
        self.cursor1.execute(self.sql, (modulo.getnivel(), modulo.getdetalles(), modulo.getlibros(), modulo.getid()))
        self.conn.commit()
        self.conn.close()

    def eliminar_modulo(self, modulo):
        self.con=con.conexion()
        self.conn=self.con.open()
        self.cursor1=self.conn.cursor()
        self.sql = "DELETE FROM modulos WHERE nivel = %s"
        self.cursor1.execute(self.sql, (modulo.getnivel(),))
        self.conn.commit()