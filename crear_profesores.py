import psycopg2

conn = None
cur = None
try:
    conn = psycopg2.connect(
        host="dpg-d3c6aab7mgec73a8p0dg-a.oregon-postgres.render.com",
        database="dbprofesores_x3qm",
        user="dbprofesores_x3qm_user",
        password="fi9u9iDsuXDPfSzZDPyijSpLVCn5K3rY",
        port=5432
    )
    cur = conn.cursor()

    sql = """
    CREATE TABLE IF NOT EXISTS profesores (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(100) NOT NULL,
        perfil VARCHAR(100) NOT NULL,
        horario VARCHAR(100) NOT NULL,
        contrasenia VARCHAR(12) NOT NULL,
        contacto VARCHAR(12) NOT NULL
    );
    ALTER SEQUENCE profesores_id_seq RESTART WITH 25640;
    """

    cur.execute(sql)
    conn.commit()
    print("Tabla 'profesores' creada correctamente.")

except psycopg2.Error as e:
    print("Error:", e)

finally:
    if cur: cur.close()
    if conn: conn.close()
