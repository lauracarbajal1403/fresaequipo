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
    CREATE TABLE IF NOT EXISTS alumnos (
        id SERIAL PRIMARY KEY,
        nombre VARCHAR(150) NOT NULL,
        nomina INT,
        profesor_id INTEGER NOT NULL,
        horario VARCHAR(100) NOT NULL,
        estado VARCHAR(50) DEFAULT 'activo',
        CONSTRAINT fk_profesor FOREIGN KEY (profesor_id)
            REFERENCES profesores(id) ON UPDATE CASCADE ON DELETE RESTRICT
    );

    ALTER SEQUENCE alumnos_id_seq RESTART WITH 1000;
    ALTER TABLE alumnos ADD COLUMN IF NOT EXISTS nomina INT;
    ALTER TABLE alumnos ADD COLUMN IF NOT EXISTS estado VARCHAR(50) DEFAULT 'activo';
    """

    cur.execute(sql)
    conn.commit()
    print("Tabla 'alumnos' creada correctamente.")

except psycopg2.Error as e:
    print("Error:", e)

finally:
    if cur: cur.close()
    if conn: conn.close()
