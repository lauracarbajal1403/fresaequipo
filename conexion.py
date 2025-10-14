import psycopg2

class conexion:
    def __init__(self):
        self.user="dbprofesores_x3qm_user"
        self.password = "fi9u9iDsuXDPfSzZDPyijSpLVCn5K3rY"
        self.database = "dbprofesores_x3qm"
        self.host = "dpg-d3c6aab7mgec73a8p0dg-a.oregon-postgres.render.com"
        self.port = "5432"
        self.sslmode = 'require'
    def open(self):
        self.conn = psycopg2.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database,
            port=self.port
        )
        return self.conn
    def close(self):
        self.conn.close()
