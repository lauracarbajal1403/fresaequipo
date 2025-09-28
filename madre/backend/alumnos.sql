CREATE TABLE alumnos (
    codigo SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    nomina INT,
    codpro INT,
    horario VARCHAR(100) NOT NULL
);