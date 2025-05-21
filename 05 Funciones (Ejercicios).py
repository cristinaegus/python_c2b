# 1. Calculadora Simple:
"""
Crea una función que pueda realizar operaciones básicas como suma, resta, 
multiplicación y división. 
Pedirá al usuario elegir una operación a partir de un listado y luego pedirá los valores a operar.


Utiliza funciones separadas para cada operación.
"""
print("""
    Elige la operación a realizar:
      1 = Suma
      2 = Resta
      3 = Multiplicación
      4 = División
""")

def pedir_numeros():
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    return num1, num2

def sumar():
    print("suma")
    num1, num2 = pedir_numeros()
    print(f"El resultado es: {num1 + num2}")

def restar():
    print("suma")
    num1, num2 = pedir_numeros()
    print(f"El resultado es: {num1 - num2}")

def multiplicar():
    print("suma")
    num1, num2 = pedir_numeros()
    print(f"El resultado es: {num1 * num2}")

def dividir():
    print("suma")
    num1, num2 = pedir_numeros()
    if num2 == 0:
        print("No se puede dividir por cero")
        return
    else:
        print(f"El resultado es: {num1 / num2}")

def salir():
    pass

def calculadora():
    while True:
        print("""
            Elige la operación a realizar:
            1 = Suma
            2 = Resta
            3 = Multiplicación
            4 = División
            5 = Salir
        """)
        operaciones = {"1": sumar, "2": restar, "3": multiplicar, "4": dividir , "5": salir}
        opcion = input("Ingrese la opción: ")
        if opcion not in operaciones.keys():
            print("Opción no válida")
            continue
        if opcion =="5":
            break
        else:
            operacion = operaciones[opcion]
            operacion()

calculadora()




# 2. Número Primo:
"""
Escribe una función que determine si un número dado es primo o no. 
Pedirá al usuario que ingrese un número y muestra un mensaje 
indicando si es primo o no.
"""
def es_primo(numero):
    if numero == 1:
        return False
    factor = 2
    while factor < numero:
        if numero % factor == 0:
            print(f"{numero} no es primo", factor)
            return False
        factor += 1
    return True

def verifica_primo():
    numero = int(input("Ingrese un número: "))
    if es_primo(numero):
        print(f"{numero} es primo")

verifica_primo()


# 3. Cálculo del Área:
"""
Implementa funciones para calcular el área de diferentes formas geométricas 
como círculo, cuadrado y triángulo. Pide al usuario que elija la forma y 
luego ingrese los valores necesarios.
"""

print("""
    Opcion
        1 : Circulo
        2 : Cuadrado
        3 : Triángulo
        q : Salir
""")
from math import pi as PI


def area_circulo():
    radio = float(input("Ingrese el radio del círculo: "))
    area = PI * radio ** 2
    print(f"El área del círculo es: {area}")

def area_cuadrado():
    lado = float(input("Ingrese el lado del cuadrado: "))
    area = lado ** 2
    print(f"El área del cuadrado es: {area}")

def area_triangulo():
    base = float(input("Ingrese la base del triángulo: "))
    altura = float(input("Ingrese la altura del triángulo: "))
    area = (base * altura) / 2
    print(f"El área del triángulo es: {area}")  

def calculadora_areas():
    while True:
        print("""
            Opcion
                1 : Circulo
                2 : Cuadrado
                3 : Triángulo
                q : Salir
        """)
        opcion = input("Ingrese la opción deseada: ")
        match opcion:
            case "1":
                area_circulo()
            case "2":
                area_cuadrado()
            case "3":
                area_triangulo()
            case "q":
                print("Saliendo...")
                break
            case _:
                print("Opción no válida")
calculadora_areas()









# 4. Inversión de Cadena:
"""
Crea una función que tome una cadena como entrada y devuelva la cadena invertida. 
Por ejemplo, si la entrada es "python", la salida debería ser "nohtyp".
"""









# 5. Contador de Palabras:
"""
Desarrolla una función que cuente el número de palabras en una oración. 
Pide al usuario que ingrese una oración y muestra el resultado.
"""











# 6. Fibonacci:
"""
Implementa una función para generar los primeros n números de la 
secuencia de Fibonacci. Pide al usuario que ingrese el valor de n.
"""



# 7. Ordenar Lista:
"""
Escribe una función que ordene una lista de números de manera ascendente 
o descendente según la elección del usuario.
"""


# 8. Factorial:
"""
Crea una función para calcular el factorial de un número. 
Pide al usuario que ingrese un número y muestra el resultado.
"""

# 9. Conversión de Temperatura:
"""
Implementa funciones para convertir entre Celsius y Fahrenheit. 
Pide al usuario que ingrese la temperatura y la unidad, y luego 
realiza la conversión.
"""

# 10. Juego de Adivinanzas:
"""
Desarrolla un juego simple en el que el programa elige un número aleatorio 
y el jugador tiene que adivinarlo. 
Proporciona pistas sobre si el número es mayor o menor. 
Utiliza funciones para organizar el código.
"""
