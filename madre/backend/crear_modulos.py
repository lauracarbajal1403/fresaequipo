import psycopg2

conn = None
cur = None
try:
    # Conexión a la base de datos
    conn = psycopg2.connect(
        host="dpg-d3c6aab7mgec73a8p0dg-a.oregon-postgres.render.com",
        database="dbprofesores_x3qm",
        user="dbprofesores_x3qm_user",
        password="fi9u9iDsuXDPfSzZDPyijSpLVCn5K3rY",
        port=5432
    )
    cur = conn.cursor()

    # Sentencia SQL para crear la tabla "modulos"
    sql = """
    CREATE TABLE IF NOT EXISTS modulos (
        nivel VARCHAR(15) PRIMARY KEY,
        detalles VARCHAR(200),
        libros INT
    );
    """

    # Ejecutar SQL
    cur.execute(sql)
    conn.commit()
    print("Tabla 'modulos' creada correctamente.")

except psycopg2.Error as e:
    print("Error al crear la tabla:", e)

finally:
    if cur:
        cur.close()
    if conn:
        conn.close()
