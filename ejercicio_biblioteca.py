from biblioteca import Libro
from biblioteca import Revista
from biblioteca import DVD

from datetime import date


libro1 = Libro("El Quijote", "12345", "Miguel de Cervantes", "978-3-16-148410-0", 500)
revista1 = Revista("National Geographic", "67890", date(2010, 7, 16), 125)
dvd1 = DVD("Inception", "11223", 148, "Christopher Nolan")
libro1.mostrar_info()
revista1.mostrar_info()
dvd1.mostrar_info()
libro1.prestar()
libro1.mostrar_info()
libro1.devolver()
libro1.mostrar_info()   

lista_materiales = [libro1, revista1, dvd1]
for elemento in lista_materiales:
    elemento.mostrar_info()


libro1.trasladar("Sala de Lectura")
libro1.mostrar_info()


while True:
    print("1. Agregar material")
    print("2. Listar materiales")
    print("3. Buscar material")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")
    if opcion == '1':
        tipo = input("Ingrese el tipo de material (libro, revista, DVD): ").lower()
        titulo = input("Ingrese el título: ")
        codigo_inventario = input("Ingrese el codigo_inventario: ")
        if tipo == 'libro':
            autor = input("Ingrese el autor: ")
            num_paginas = int(input("Ingrese el número de páginas: "))
            isbn = input("Ingrese el ISBN: ")
            material = Libro(titulo, codigo_inventario, autor, isbn, num_paginas)
        elif tipo == 'revista':
            fecha_publicacion = input("Ingrese la fecha de publicación: ")
            numero_edicion = input("Ingrese el número de edición: ")
            material = Revista(titulo, codigo_inventario, fecha_publicacion, numero_edicion)
        elif tipo == 'dvd':
            duracion = int(input("Ingrese la duración en minutos: "))
            director = input("Ingrese el director: ")
            material = DVD(titulo, codigo_inventario, duracion, director)
        else:
            print("Tipo de material no válido.")
            continue
        lista_materiales.append(material)
    elif opcion == '2':
        for elemento in lista_materiales:
            elemento.mostrar_info()
    elif opcion == '3':
        codigo_inventario = input("Ingrese el codigo_inventario del material: ")
        for material in lista_materiales:
            if material.codigo_inventario == codigo_inventario:
                material.mostrar_info()
    elif opcion == '4':
        print("Saliendo del programa.")
        break
    else:
        print("Opción no válida. Intente de nuevo.")

