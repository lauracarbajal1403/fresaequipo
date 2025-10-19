import psycopg2
import conexion as con

class dbprofesores:
    def nuevo_profesor(self, profe):        
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor = self.conn.cursor()
            self.sql = "INSERT INTO profesores (nombre, contrasenia, contacto, perfil, horario) VALUES ( %s, %s, %s, %s, %s)"
            self.datos = (
                profe.nombre, 
                profe.contrasenia,
                profe.contacto,
                profe.perfil,
                profe.horario
            )
            self.cursor.execute(self.sql, self.datos)
            self.conn.commit()
        except psycopg2.Error as e:
            print(f"Error al guardar alumno: {e}")
        finally:
            self.conn.close()

    def buscar_profesor(self, profe):
        try:
            self.con = con.conexion()
            self.conn = self.con.open()
            self.cursor1=self.conn.cursor()
            auxi=None
            self.sql = "SELECT * FROM profesores WHERE nombre = %s"
            self.cursor1.execute(self.sql, (profe.nombre,))
            row = self.cursor1.fetchone()
            self.conn.commit()
            self.conn.close()
            print("wow")
            if row[1] is not None:
                print("ok")
                profe.setide(row[0])
                profe.setnombrepro(row[1])
                profe.setpassw(row[2])
                profe.setcontacto(row[3])
                profe.setperfil(row[4])
                profe.sethorario(row[5])
        except Exception as e:
            print(f"Error al buscar profesor: {e}")
            return None
        return profe

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
    
    def eliminar_profesor(self, id_profesor):
        self.con=con.conexion()
        self.conn=self.con.open()
        self.cursor1=self.conn.cursor()
        self.sql = "DELETE FROM profesores WHERE id = %s"
        self.cursor1.execute(self.sql, (id_profesor,))
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
            self.sql = "SELECT * FROM profesores WHERE id = %s"
            self.cursor1.execute(self.sql, (profe.id,))
            print("ok")
            row = self.cursor1.fetchone()
            self.conn.commit()
            self.conn.close()
            if row is not None:
                print("quiza")
                if profe.contrasenia==row[4]:
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
    