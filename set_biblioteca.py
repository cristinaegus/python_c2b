import psycopg2

# Leer CONN_STR desde un archivo .env
from dotenv import load_dotenv
import os
load_dotenv()
CONN_STR = os.getenv('CONN_STR')

# Conexión a la base de datos
conexion = psycopg2.connect(CONN_STR)

cursor = conexion.cursor()

# Crear tabla de materiales
cursor.execute("""
CREATE TABLE IF NOT EXISTS materiales (
    codigo_inventario VARCHAR(10) PRIMARY KEY,
    titulo TEXT NOT NULL,
    tipo TEXT NOT NULL,
    autor TEXT,
    isbn TEXT,
    numero_paginas INTEGER,
    fecha_publicacion TEXT,
    numero_edicion TEXT,
    duracion INTEGER,
    director TEXT,
    disponible BOOLEAN DEFAULT TRUE
)
""")

# Crear tabla de usuarios
cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id_usuario VARCHAR(10) PRIMARY KEY,
    nombre TEXT NOT NULL,
    apellido TEXT NOT NULL
)
""")

# Crear tabla de préstamos
cursor.execute("""
CREATE TABLE IF NOT EXISTS prestamos (
    id SERIAL PRIMARY KEY,
    id_usuario VARCHAR(10) REFERENCES usuarios(id_usuario),
    id_material VARCHAR(10) REFERENCES materiales(codigo_inventario),
    fecha_prestamo TIMESTAMP NOT NULL,
    fecha_devolucion TIMESTAMP NOT NULL
)
""")

conexion.commit()
cursor.close()
conexion.close()

print("Tablas creadas correctamente.")
