CREATE TABLE profesores (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    materia VARCHAR(100) NOT NULL,
    horario VARCHAR(100) NOT NULL,
    contrasenia VARCHAR(100) NOT NULL
);
