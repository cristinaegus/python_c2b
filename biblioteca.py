# biblioteca.py
from abc import ABC, abstractmethod
from datetime import datetime, timedelta
import uuid
import comunicacion_biblioteca as db

class MaterialBiblioteca(ABC):
    def __init__(self, titulo, codigo_inventario, ubicacion=None):
        self.titulo = titulo
        self.__ubicacion = ubicacion
        self.codigo_inventario = codigo_inventario
        self.disponible = True

    @property
    def ubicacion(self):
        print(f"Tienes permiso para ver la ubicacion del item '{self.titulo}'.")
        return self.__ubicacion

    @ubicacion.setter
    def ubicacion(self, nueva_ubicacion):
        print(f"Compruebo que la ubicación está disponible para el item '{self.titulo}'.")
        self.__ubicacion = nueva_ubicacion

    def trasladar(self, nueva_ubicacion):
        self.ubicacion = nueva_ubicacion
        print(f"El item '{self.titulo}' ha sido trasladado a '{nueva_ubicacion}'.")

    def prestar(self):
        if self.disponible:
            self.disponible = False
            print(f"El item '{self.titulo}' ha sido prestado.")
        else:
            print(f"El item '{self.titulo}' no está disponible.")

    def devolver(self):
        self.disponible = True
        print(f"El item '{self.titulo}' ha sido devuelto.")

    @abstractmethod
    def mostrar_info(self):
        print(f"Título: {self.titulo}")
        print(f"Código de inventario: {self.codigo_inventario}")
        print(f"Ubicación: {self.ubicacion}")
        print(f"Disponible: {'Sí' if self.disponible else 'No'}")


class Libro(MaterialBiblioteca):
    def __init__(self, titulo, codigo_inventario, autor, isbn, numero_paginas):
        super().__init__(titulo, codigo_inventario)
        self.autor = autor
        self.numero_paginas = numero_paginas
        self.isbn = isbn

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.isbn}")
        print(f"Número de páginas: {self.numero_paginas}")


class Revista(MaterialBiblioteca):
    def __init__(self, titulo, codigo_inventario, fecha_publicacion, numero_edicion):
        super().__init__(titulo, codigo_inventario)
        self.numero_edicion = numero_edicion
        self.fecha_publicacion = fecha_publicacion

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Número: {self.numero_edicion}")
        print(f"Fecha de publicación: {self.fecha_publicacion}")


class DVD(MaterialBiblioteca):
    def __init__(self, titulo, codigo_inventario, duracion, director):
        super().__init__(titulo, codigo_inventario)
        self.duracion = duracion
        self.director = director

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Duración: {self.duracion} minutos")
        print(f"Director: {self.director}")


class Usuario:
    def __init__(self, nombre, apellido, id_usuario=None):
        self.nombre = nombre
        self.apellido = apellido
        self.id_usuario = id_usuario or uuid.uuid4().hex[:6].upper()

    def mostrar_info(self):
        print(f"{self.nombre} {self.apellido} ID Usuario: {self.id_usuario}")


class Prestamo:
    def __init__(self, id_usuario, id_material):
        self.id_usuario = id_usuario
        self.id_material = id_material
        self.fecha_prestamo = datetime.now()
        self.fecha_devolucion = self.fecha_prestamo + timedelta(days=14)

    def mostrar_info(self):
        print(f"Usuario: {self.id_usuario}")
        print(f"Material: {self.id_material}")
        print(f"Fecha de préstamo: {self.fecha_prestamo}")
        print(f"Fecha de devolución: {self.fecha_devolucion}")


class GestorBiblioteca:
    def agregar_material(self, material):
        db.agregar_material(material)

    def mostrar_materiales(self):
        materiales = db.listar_materiales()
        for datos in materiales:
            tipo = datos[2]
            if tipo == 'libro':
                mat = Libro(datos[1], datos[0], datos[3], datos[4], datos[5])
            elif tipo == 'revista':
                mat = Revista(datos[1], datos[0], datos[6], datos[7])
            elif tipo == 'dvd':
                mat = DVD(datos[1], datos[0], datos[8], datos[9])
            else:
                continue
            mat.disponible = datos[10]
            mat.mostrar_info()

    def buscar_material(self, codigo_inventario):
        datos = db.buscar_material(codigo_inventario)
        if datos:
            tipo = datos[2]
            if tipo == 'libro':
                mat = Libro(datos[1], datos[0], datos[3], datos[4], datos[5])
            elif tipo == 'revista':
                mat = Revista(datos[1], datos[0], datos[6], datos[7])
            elif tipo == 'dvd':
                mat = DVD(datos[1], datos[0], datos[8], datos[9])
            else:
                print("Tipo de material desconocido.")
                return
            mat.disponible = datos[10]
            mat.mostrar_info()
        else:
            print("Material no encontrado.")

    def borrar_material(self, codigo_inventario):
        datos = db.buscar_material(codigo_inventario)
        if datos:
            print("¿Está seguro de querer borrar este material?")
            print(f"Título: {datos[1]} - Tipo: {datos[2]}")
            confirmacion = input("Ingrese 'si' para confirmar: ")
            if confirmacion.lower() == 'si':
                db.borrar_material(codigo_inventario)
                print("Material borrado.")
        else:
            print("Material no encontrado.")

    def agregar_usuario(self, usuario):
        db.agregar_usuario(usuario)

    def mostrar_usuarios(self):
        usuarios = db.listar_usuarios()
        for u in usuarios:
            usuario = Usuario(u[1], u[2], id_usuario=u[0])
            usuario.mostrar_info()

    def prestar_material(self, id_usuario, id_material):
        db.agregar_prestamo(id_usuario, id_material)

    def mostrar_prestamos(self):
        prestamos = db.listar_prestamos()
        for p in prestamos:
            print(f"Usuario: {p[1]} - Material: {p[2]}")
            print(f"Fecha de préstamo: {p[3]}")
            print(f"Fecha de devolución: {p[4]}")
            print("-" * 40)
