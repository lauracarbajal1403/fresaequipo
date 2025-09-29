CREATE TABLE profesores (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    perfil VARCHAR(100) NOT NULL,
    horario VARCHAR(100) NOT NULL,
    contrasenia VARCHAR(12) NOT NULL,
    contacto VARCHAR(12) NOT NULL
);
