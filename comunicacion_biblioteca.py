import psycopg2
from datetime import datetime, timedelta

# Leer CONN_STR desde un archivo .env
from dotenv import load_dotenv
import os
load_dotenv()
CONN_STR = os.getenv('CONN_STR')

def conectar():
    return psycopg2.connect(CONN_STR)

### Materiales ###
def agregar_material(material):
    conn = conectar()
    cur = conn.cursor()
    tipo = material.__class__.__name__.lower()
    
    cur.execute("""
        INSERT INTO materiales (
            codigo_inventario, titulo, tipo, autor, isbn, numero_paginas,
            fecha_publicacion, numero_edicion, duracion, director, disponible
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        material.codigo_inventario,
        material.titulo,
        tipo,
        getattr(material, 'autor', None),
        getattr(material, 'isbn', None),
        getattr(material, 'numero_paginas', None),
        getattr(material, 'fecha_publicacion', None),
        getattr(material, 'numero_edicion', None),
        getattr(material, 'duracion', None),
        getattr(material, 'director', None),
        material.disponible
    ))

    conn.commit()
    cur.close()
    conn.close()

def listar_materiales():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT * FROM materiales")
    materiales = cur.fetchall()
    cur.close()
    conn.close()
    return materiales

def buscar_material(codigo):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT * FROM materiales WHERE codigo_inventario = %s", (codigo,))
    material = cur.fetchone()
    cur.close()
    conn.close()
    return material

def borrar_material(codigo):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("DELETE FROM materiales WHERE codigo_inventario = %s", (codigo,))
    conn.commit()
    cur.close()
    conn.close()

### Usuarios ###
def agregar_usuario(usuario):
    conn = conectar()
    cur = conn.cursor()
    cur.execute("INSERT INTO usuarios (id_usuario, nombre, apellido) VALUES (%s, %s, %s)",
                (usuario.id_usuario, usuario.nombre, usuario.apellido))
    conn.commit()
    cur.close()
    conn.close()

def listar_usuarios():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT * FROM usuarios")
    usuarios = cur.fetchall()
    cur.close()
    conn.close()
    return usuarios

### Préstamos ###
def agregar_prestamo(id_usuario, id_material):
    conn = conectar()
    cur = conn.cursor()
    fecha_prestamo = datetime.now()
    fecha_devolucion = fecha_prestamo + timedelta(days=14)
    cur.execute("""
        INSERT INTO prestamos (id_usuario, id_material, fecha_prestamo, fecha_devolucion)
        VALUES (%s, %s, %s, %s)
    """, (id_usuario, id_material, fecha_prestamo, fecha_devolucion))
    conn.commit()
    cur.close()
    conn.close()

def listar_prestamos():
    conn = conectar()
    cur = conn.cursor()
    cur.execute("SELECT * FROM prestamos")
    prestamos = cur.fetchall()
    cur.close()
    conn.close()
    return prestamos
