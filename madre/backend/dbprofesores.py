import mysql.connector
import conexion as con

class dbprofesores:
    def nuevo_profesor(self, profe):        
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "INSERT INTO profesores (idempleado, nombre, password, contacto, perfil, horario) VALUES ( %s, %s, %s, %s, %s, %s)"
            self.datos = (
                profe.id,
                profe.nombre, 
                profe.contrasenia,
                profe.contacto,
                profe.perfil,
                profe.horario
            )
            self.cursor.execute(self.sql, self.datos)
            self.conn.commit()
        except mysql.connector.Error as e:
            print(f"Error al guardar alumno: {e}")
        finally:
            self.conn.close()

    """
    def buscar_profesor(self, profe):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1=self.conn.cursor()
            auxi=None
            self.sql = "SELECT * FROM profesores WHERE idempleado = %s"
            self.cursor1.execute(self.sql, (profe.id))
            row = self.cursor1.fetchone()
            self.conn.commit()
            self.conn.close()
            print("wow")
            if row[2] is not None:
                print("ok")
                auxi = pro.profesores()
                auxi.setide(row[0])
                auxi.setnombrepro(row[1])
                auxi.setpassw(row[2])
                auxi.setcontacto(row[3])
                auxi.setperfil(row[4])
                auxi.sethorario(row[5])
        except Exception as e:
            print(f"Error al buscar alumno: {e}")
            return None
        return auxi
    """
    def editar_profesor(self, profe):
        self.con=con.conexion()
        self.conn=self.con.open()
        self.cursor1=self.conn.cursor()
        self.sql="update profesores set password=%s,perfil=%s, horario = %s where idempleado={}".format(profe.getide())
        self.datos=(profe.contrasenia,
                    profe.perfil,
                    profe.horario)
        self.cursor1.execute(self.sql, self.datos)
        self.conn.commit()
        self.conn.close()
    
    def eliminar_profesor(self, profe):
        self.con=con.conexion()
        self.conn=self.con.open()
        self.cursor1=self.conn.cursor()
        self.sql = "DELETE FROM profesores WHERE idempleado = %s"
        self.cursor1.execute(self.sql, (profe.id,))
        self.conn.commit()

    def getid_profesor(self):
        id=1
        self.con=con.conexion()
        self.conn=self.con.open()
        self.cursor=self.conn.cursor()
        self.sql="select max(idempleado) as id from profesores"
        self.cursor.execute(self.sql)
        row=self.cursor.fetchone()
        self.cursor.close()
        self.conn.close()
        if row[0] is None:
            return 1
        else:
            return row[0] + 1
    
    def autentificar(self, profe):
        try:
            self.con = con.conexion()
            self.conn=self.con.open()
            self.cursor1=self.conn.cursor()
            aux=None
            self.sql = "SELECT * FROM profesores WHERE idempleado = %s"
            self.cursor1.execute(self.sql, (profe.id,))
            print("ok")
            row = self.cursor1.fetchone()
            self.conn.commit()
            self.conn.close()
            if row is not None:
                print("quiza")
                if profe.contrasenia==row[2]:
                    print("hola")
                    return {
                        "id": int(row[0]),
                        "nombre": row[1],
                        "horario": row[5],
                        "contacto": row[3],
                        "perfil": row[4]
                    }
                else:
                    print("Error", "Contraseña incorrecta")
            else:
                print("Error", "Usuario no encontrado")
        except:
            print("NOOOOOO")
    