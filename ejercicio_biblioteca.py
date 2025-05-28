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

libro1.trasladar("Sala de Lectura")
libro1.mostrar_info()