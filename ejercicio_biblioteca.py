from biblioteca import GestorBiblioteca, Libro, Revista, DVD, Usuario
import uuid

app = GestorBiblioteca()

while True:
    print("\n====== Menú Biblioteca ======")
    print("1. Agregar material")
    print("2. Listar materiales")
    print("3. Buscar material")
    print("4. Borrar material")
    print("5. Agregar usuario")
    print("6. Listar usuarios")
    print("7. Agregar préstamo")
    print("8. Listar préstamos")
    print("q. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        tipo = input("Ingrese el tipo de material (libro, revista, dvd): ").lower()
        titulo = input("Ingrese el título: ")
        codigo_inventario = uuid.uuid4().hex[:6].upper()

        if tipo == 'libro':
            autor = input("Ingrese el autor: ")
            num_paginas = int(input("Ingrese el número de páginas: "))
            isbn = input("Ingrese el ISBN: ")
            material = Libro(titulo, codigo_inventario, autor, isbn, num_paginas)

        elif tipo == 'revista':
            fecha_publicacion = input("Ingrese la fecha de publicación (YYYY-MM-DD): ")
            numero_edicion = input("Ingrese el número de edición: ")
            material = Revista(titulo, codigo_inventario, fecha_publicacion, numero_edicion)

        elif tipo == 'dvd':
            duracion = int(input("Ingrese la duración en minutos: "))
            director = input("Ingrese el director: ")
            material = DVD(titulo, codigo_inventario, duracion, director)

        else:
            print("Tipo de material no válido.")
            continue

        app.agregar_material(material)
        print(f"Material '{material.titulo}' agregado con código {material.codigo_inventario}.")

    elif opcion == '2':
        app.mostrar_materiales()

    elif opcion == '3':
        codigo_inventario = input("Ingrese el código de inventario del material: ")
        app.buscar_material(codigo_inventario)

    elif opcion == '4':
        codigo_inventario = input("Ingrese el código de inventario del material a borrar: ")
        app.borrar_material(codigo_inventario)

    elif opcion == '5':
        nombre = input("Ingrese el nombre del usuario: ")
        apellido = input("Ingrese el apellido del usuario: ")
        usuario = Usuario(nombre, apellido)
        app.agregar_usuario(usuario)
        print(f"Usuario '{usuario.nombre} {usuario.apellido}' agregado con ID {usuario.id_usuario}.")

    elif opcion == '6':
        app.mostrar_usuarios()

    elif opcion == '7':
        id_usuario = input("Ingrese el ID del usuario: ")
        id_material = input("Ingrese el código de inventario del material: ")
        app.prestar_material(id_usuario, id_material)

    elif opcion == '8':
        app.mostrar_prestamos()

    elif opcion == 'q':
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida. Intente de nuevo.")
