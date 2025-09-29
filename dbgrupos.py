import conexion as con
import psycopg2

class dbgrupos:
    def nuevo_grupo(self, grupo):        
        conn = None
        try:
            self.con = con.conexion()
            conn = self.con.open()
            if conn is None:
                return
            cursor = conn.cursor()
            sql = "INSERT INTO grupos (id, grupo, horario) VALUES (%s, %s, %s)"
            datos = (grupo.id, grupo.grupo)
            cursor.execute(sql, datos)
            conn.commit()
        except psycopg2.Error as e:
            print(f"Error al guardar grupo: {e}")
        finally:
            if conn:
                conn.close()

    """
    def buscar_grupo(self, grupo):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1=self.conn.cursor()
            auxi=None
            self.sql = "SELECT * FROM grupos WHERE id = %s"
            self.cursor1.execute(self.sql, (grupo.getid(),))
            row = self.cursor1.fetchone()
            self.conn.commit()
            self.conn.close()
            print("wow")
            if row[0] is not None:
                print("ok")
                auxi = gr.grupos()
                auxi.setid(row[0])
                auxi.sethorario(row[1])
        except Exception as e:
            print(f"Error al buscar grupo: {e}")
            return None
        return auxi
    """
    def editar_grupo(self, grupo):
        self.con=con.conexion()
        self.conn=self.con.open()
        self.cursor1=self.conn.cursor()
        self.sql="update grupos set grupo=%s where id=%s"
        self.cursor1.execute(self.sql, (grupo.horario, grupo.id))
        self.conn.commit()
        self.conn.close()
    
    def eliminar_grupo(self, grupo):
        self.con=con.conexion()
        self.conn=self.con.open()
        self.cursor1=self.conn.cursor()
        self.sql = "DELETE FROM grupos WHERE id = %s"
        self.cursor1.execute(self.sql, (grupo.id,))
        self.conn.commit()

    def getid_grupo(self):
        id=1
        self.con=con.conexion()
        self.conn=self.con.open()
        self.cursor=self.conn.cursor()
        self.sql="select max(id) as id from grupos"
        self.cursor.execute(self.sql)
        row=self.cursor.fetchone()
        self.cursor.close()
        self.conn.close()
        if row[0] is None:
            return 1
        else:
            return row[0] + 1