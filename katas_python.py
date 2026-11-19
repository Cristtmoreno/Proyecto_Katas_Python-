"""
PROYECTO LÓGICA: Katas de Python.

Ejercicios resueltos. Cada ejercicio va encabezado por su enunciado.
Los ejercicios que piden datos al usuario (8, 11, 31, 38, 39, 41) están
dentro de funciones y solo se ejecutan si se activa MODO_INTERACTIVO.
"""

from functools import reduce
import math

MODO_INTERACTIVO = False


# 1. Escribe una función que reciba una cadena de texto como parámetro y
# devuelva un diccionario con las frecuencias de cada letra en la cadena.
# Los espacios no deben ser considerados.
def frecuencia_letras(texto):
    """Devuelve un diccionario {letra: frecuencia} sin contar espacios."""
    frecuencias = {}
    for caracter in texto:
        if caracter != " ":
            frecuencias[caracter] = frecuencias.get(caracter, 0) + 1
    return frecuencias


# 2. Dada una lista de números, obtén una nueva lista con el doble de cada
# valor. Usa la función map()
def doblar_valores(numeros):
    """Devuelve una lista con el doble de cada número."""
    return list(map(lambda x: x * 2, numeros))


# 3. Escribe una función que tome una lista de palabras y una palabra objetivo
# como parámetros. La función debe devolver una lista con todas las palabras de
# la lista original que contengan la palabra objetivo.
def palabras_que_contienen(palabras, objetivo):
    """Devuelve las palabras que contienen la palabra objetivo."""
    return [palabra for palabra in palabras if objetivo in palabra]


# 4. Genera una función que calcule la diferencia entre los valores de dos
# listas. Usa la función map()
def diferencia_listas(lista1, lista2):
    """Resta elemento a elemento lista1 - lista2."""
    return list(map(lambda a, b: a - b, lista1, lista2))


# 5. Escribe una función que tome una lista de números como parámetro y un
# valor opcional nota_aprobado, que por defecto es 5. La función debe calcular
# la media de los números en la lista y determinar si la media es mayor o igual
# que nota aprobado. Si es así, el estado será "aprobado", de lo contrario,
# será "suspenso". La función debe devolver una tupla que contenga la media y
# el estado.
def evaluar_notas(notas, nota_aprobado=5):
    """Devuelve (media, estado)."""
    media = sum(notas) / len(notas)
    estado = "aprobado" if media >= nota_aprobado else "suspenso"
    return media, estado


# 6. Escribe una función que calcule el factorial de un número de manera
# recursiva.
def factorial(n):
    """Factorial recursivo de n (n >= 0)."""
    if n < 0:
        raise ValueError("El factorial no está definido para negativos.")
    if n in (0, 1):
        return 1
    return n * factorial(n - 1)


# 7. Genera una función que convierta una lista de tuplas a una lista de
# strings. Usa la función map()
def tuplas_a_strings(tuplas):
    """Convierte cada tupla en un string con sus elementos separados por espacios."""
    return list(map(lambda t: " ".join(map(str, t)), tuplas))


# 8. Escribe un programa que pida al usuario dos números e intente dividirlos.
# Si el usuario ingresa un valor no numérico o intenta dividir por cero, maneja
# esas excepciones de manera adecuada. Asegúrate de mostrar un mensaje
# indicando si la división fue exitosa o no.
def dividir_numeros_usuario():
    """Pide dos números y los divide gestionando errores."""
    try:
        dividendo = float(input("Introduce el dividendo: "))
        divisor = float(input("Introduce el divisor: "))
        resultado = dividendo / divisor
    except ValueError:
        print("Error: debes introducir valores numéricos. La división no fue exitosa.")
    except ZeroDivisionError:
        print("Error: no se puede dividir por cero. La división no fue exitosa.")
    else:
        print(f"División exitosa. Resultado: {resultado}")


# 9. Escribe una función que tome una lista de nombres de mascotas como
# parámetro y devuelva una nueva lista excluyendo ciertas mascotas prohibidas
# en España. La lista de mascotas a excluir es ["Mapache", "Tigre",
# "Serpiente Pitón", "Cocodrilo", "Oso"]. Usa la función filter()
MASCOTAS_PROHIBIDAS = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]


def filtrar_mascotas(mascotas):
    """Excluye las mascotas prohibidas."""
    return list(filter(lambda m: m not in MASCOTAS_PROHIBIDAS, mascotas))


# 10. Escribe una función que reciba una lista de números y calcule su
# promedio. Si la lista está vacía, lanza una excepción personalizada y maneja
# el error adecuadamente.
class ListaVaciaError(Exception):
    """Excepción lanzada cuando la lista está vacía."""


def promedio_seguro(numeros):
    """Calcula el promedio; lanza ListaVaciaError si la lista está vacía."""
    if not numeros:
        raise ListaVaciaError("La lista está vacía, no se puede calcular el promedio.")
    return sum(numeros) / len(numeros)


def probar_promedio_seguro(numeros):
    """Maneja la excepción personalizada."""
    try:
        return promedio_seguro(numeros)
    except ListaVaciaError as error:
        print(f"Error: {error}")
        return None


# 11. Escribe un programa que pida al usuario que introduzca su edad. Si el
# usuario ingresa un valor no numérico o un valor fuera del rango esperado
# (por ejemplo, menor que 0 o mayor que 120), maneja las excepciones
# adecuadamente.
def validar_edad(valor):
    """Convierte y valida una edad; lanza ValueError si no es válida."""
    edad = int(valor)
    if edad < 0 or edad > 120:
        raise ValueError("La edad debe estar entre 0 y 120.")
    return edad


def pedir_edad():
    """Pide la edad al usuario y gestiona los errores."""
    try:
        edad = validar_edad(input("Introduce tu edad: "))
    except ValueError as error:
        print(f"Edad no válida: {error}")
    else:
        print(f"Tu edad es {edad} años.")


# 12. Genera una función que al recibir una frase devuelva una lista con la
# longitud de cada palabra. Usa la función map()
def longitud_palabras(frase):
    """Devuelve la longitud de cada palabra de la frase."""
    return list(map(len, frase.split()))


# 13. Genera una función la cual, para un conjunto de caracteres, devuelva una
# lista de tuplas con cada letra en mayúsculas y minúsculas. Las letras no
# pueden estar repetidas. Usa la función map()
def mayus_minus(caracteres):
    """Devuelve [(MAYÚSCULA, minúscula), ...] sin letras repetidas."""
    letras_unicas = sorted(set(c.lower() for c in caracteres if c.isalpha()))
    return list(map(lambda c: (c.upper(), c.lower()), letras_unicas))


# 14. Crea una función que retorne las palabras de una lista de palabras que
# comience con una letra en especifico. Usa la función filter()
def palabras_que_empiezan_por(palabras, letra):
    """Filtra las palabras que empiezan por la letra indicada."""
    return list(filter(lambda p: p.lower().startswith(letra.lower()), palabras))


# 15. Crea una función lambda que sume 3 a cada número de una lista dada.
sumar_tres = lambda numeros: list(map(lambda x: x + 3, numeros))


# 16. Escribe una función que tome una cadena de texto y un número entero n
# como parámetros y devuelva una lista de todas las palabras que sean más
# largas que n. Usa la función filter()
def palabras_mas_largas(texto, n):
    """Devuelve las palabras con longitud mayor que n."""
    return list(filter(lambda p: len(p) > n, texto.split()))


# 17. Crea una función que tome una lista de dígitos y devuelva el número
# correspondiente. Por ejemplo, [5,7,2] corresponde al número quinientos
# setenta y dos (572). Usa la función reduce()
def digitos_a_numero(digitos):
    """Convierte una lista de dígitos en un número entero."""
    return reduce(lambda acumulado, d: acumulado * 10 + d, digitos)


# 18. Escribe un programa en Python que cree una lista de diccionarios que
# contenga información de estudiantes (nombre, edad, calificación) y use la
# función filter para extraer a los estudiantes con una calificación mayor o
# igual a 90. Usa la función filter()
estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 95},
    {"nombre": "Luis", "edad": 22, "calificacion": 85},
    {"nombre": "Marta", "edad": 21, "calificacion": 90},
    {"nombre": "Pedro", "edad": 23, "calificacion": 70},
]
estudiantes_destacados = list(filter(lambda e: e["calificacion"] >= 90, estudiantes))


# 19. Crea una función lambda que filtre los números impares de una lista dada.
filtrar_impares = lambda numeros: list(filter(lambda x: x % 2 != 0, numeros))


# 20. Para una lista con elementos tipo integer y string obtén una nueva lista
# sólo con los valores int. Usa la función filter()
def solo_enteros(elementos):
    """Devuelve solo los elementos de tipo int."""
    return list(filter(lambda x: isinstance(x, int) and not isinstance(x, bool), elementos))


# 21. Crea una función que calcule el cubo de un número dado mediante una
# función lambda
cubo = lambda x: x ** 3


# 22. Dada una lista numérica, obtén el producto total de los valores de dicha
# lista. Usa la función reduce().
def producto_total(numeros):
    """Producto de todos los valores."""
    return reduce(lambda a, b: a * b, numeros)


# 23. Concatena una lista de palabras. Usa la función reduce().
def concatenar_palabras(palabras):
    """Concatena las palabras separándolas con un espacio."""
    return reduce(lambda a, b: a + " " + b, palabras)


# 24. Calcula la diferencia total en los valores de una lista. Usa la función
# reduce().
def diferencia_total(numeros):
    """Resta sucesiva: n0 - n1 - n2 - ..."""
    return reduce(lambda a, b: a - b, numeros)


# 25. Crea una función que cuente el número de caracteres en una cadena de
# texto dada.
def contar_caracteres(texto):
    """Número de caracteres de la cadena."""
    return len(texto)


# 26. Crea una función lambda que calcule el resto de la división entre dos
# números dados.
resto = lambda a, b: a % b


# 27. Crea una función que calcule el promedio de una lista de números.
def promedio(numeros):
    """Promedio de una lista de números."""
    return sum(numeros) / len(numeros)


# 28. Crea una función que busque y devuelva el primer elemento duplicado en
# una lista dada.
def primer_duplicado(elementos):
    """Devuelve el primer elemento que aparece repetido, o None."""
    vistos = set()
    for elemento in elementos:
        if elemento in vistos:
            return elemento
        vistos.add(elemento)
    return None


# 29. Crea una función que convierta una variable en una cadena de texto y
# enmascare todos los caracteres con el carácter '#', excepto los últimos
# cuatro.
def enmascarar(variable):
    """Enmascara con '#' todo salvo los últimos cuatro caracteres."""
    texto = str(variable)
    return "#" * max(len(texto) - 4, 0) + texto[-4:]


# 30. Crea una función que determine si dos palabras son anagramas, es decir,
# si están formadas por las mismas letras pero en diferente orden.
def son_anagramas(palabra1, palabra2):
    """True si son anagramas (mismas letras, distinto orden)."""
    p1, p2 = palabra1.lower(), palabra2.lower()
    return p1 != p2 and sorted(p1) == sorted(p2)


# 31. Crea una función que solicite al usuario ingresar una lista de nombres y
# luego solicite un nombre para buscar en esa lista. Si el nombre está en la
# lista, se imprime un mensaje indicando que fue encontrado, de lo contrario,
# se lanza una excepción.
def buscar_nombre(nombres, nombre):
    """Lanza ValueError si el nombre no está en la lista."""
    if nombre not in nombres:
        raise ValueError(f"El nombre '{nombre}' no se encuentra en la lista.")
    print(f"El nombre '{nombre}' fue encontrado.")


def buscar_nombre_usuario():
    """Versión interactiva del ejercicio 31."""
    entrada = input("Introduce nombres separados por comas: ")
    nombres = [n.strip() for n in entrada.split(",")]
    nombre = input("Nombre a buscar: ").strip()
    try:
        buscar_nombre(nombres, nombre)
    except ValueError as error:
        print(f"Error: {error}")


# 32. Crea una función que tome un nombre completo y una lista de empleados,
# busque el nombre completo en la lista y devuelve el puesto del empleado si
# está en la lista, de lo contrario, devuelve un mensaje indicando que la
# persona no trabaja aquí.
def buscar_puesto(nombre_completo, empleados):
    """empleados: lista de diccionarios con 'nombre' y 'puesto'."""
    for empleado in empleados:
        if empleado["nombre"] == nombre_completo:
            return empleado["puesto"]
    return f"{nombre_completo} no trabaja aquí."


# 33. Crea una función lambda que sume elementos correspondientes de dos listas
# dadas.
sumar_listas = lambda l1, l2: list(map(lambda a, b: a + b, l1, l2))


# 34. Crea la clase Arbol, define un árbol genérico con un tronco y ramas como
# atributos. Los métodos disponibles son: crecer_tronco, nueva_rama,
# crecer_ramas, quitar_rama e info_arbol. El objetivo es implementar estos
# métodos para manipular la estructura del árbol.
# Caso de uso: crear un árbol, crecer el tronco, añadir una rama, crecer las
# ramas, añadir dos ramas, retirar la rama en la posición 2, obtener info.
class Arbol:
    """Árbol genérico con un tronco y una lista de ramas."""

    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        self.ramas = [rama + 1 for rama in self.ramas]

    def quitar_rama(self, posicion):
        if 0 <= posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            raise IndexError("No existe una rama en esa posición.")

    def info_arbol(self):
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas,
        }


def caso_uso_arbol():
    arbol = Arbol()
    arbol.crecer_tronco()
    arbol.nueva_rama()
    arbol.crecer_ramas()
    arbol.nueva_rama()
    arbol.nueva_rama()
    arbol.quitar_rama(2)  # posición 2 interpretada como índice 2 (tercera rama)
    return arbol.info_arbol()


# 35. (El enunciado no incluye el ejercicio 35: pasa del 34 al 36.)


# 36. Crea la clase UsuarioBanco, representa a un usuario de un banco con su
# nombre, saldo y si tiene o no cuenta corriente. Proporciona métodos para
# realizar operaciones como retirar dinero, transferir dinero desde otro
# usuario y agregar dinero al saldo.
# Caso de uso: Alicia (100) y Bob (50) con cuenta corriente; agregar 20 a Bob;
# transferir 80 de Bob a Alicia; retirar 50 a Alicia.
class UsuarioBanco:
    """Usuario de banco con nombre, saldo y cuenta corriente."""

    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        if not self.cuenta_corriente:
            raise ValueError(f"{self.nombre} no tiene cuenta corriente.")
        if cantidad <= 0 or cantidad > self.saldo:
            raise ValueError(f"{self.nombre} no puede retirar {cantidad}: saldo insuficiente o cantidad no válida.")
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        """Transfiere desde otro_usuario al usuario actual."""
        if not self.cuenta_corriente:
            raise ValueError(f"{self.nombre} no tiene cuenta corriente.")
        otro_usuario.retirar_dinero(cantidad)
        self.agregar_dinero(cantidad)

    def agregar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a agregar debe ser positiva.")
        self.saldo += cantidad


def caso_uso_banco():
    alicia = UsuarioBanco("Alicia", 100, True)
    bob = UsuarioBanco("Bob", 50, True)
    bob.agregar_dinero(20)
    try:
        alicia.transferir_dinero(bob, 80)  # Bob solo tiene 70: debe fallar
    except ValueError as error:
        print(f"Transferencia fallida: {error}")
    try:
        alicia.retirar_dinero(50)
    except ValueError as error:
        print(f"Retirada fallida: {error}")
    return alicia.saldo, bob.saldo


# 37. Crea una función llamada procesar_texto que procesa un texto según la
# opción especificada: contar_palabras, reemplazar_palabras, eliminar_palabra.
# Estas opciones son otras funciones que tenemos que definir primero y llamar
# dentro de la función procesar_texto.
def contar_palabras(texto):
    """Diccionario {palabra: número de apariciones}."""
    conteo = {}
    for palabra in texto.split():
        conteo[palabra] = conteo.get(palabra, 0) + 1
    return conteo


def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    """Reemplaza palabra_original por palabra_nueva (palabras completas)."""
    return " ".join(palabra_nueva if p == palabra_original else p for p in texto.split())


def eliminar_palabra(texto, palabra):
    """Elimina todas las apariciones de la palabra."""
    return " ".join(p for p in texto.split() if p != palabra)


def procesar_texto(texto, opcion, *args):
    """opcion: 'contar', 'reemplazar' o 'eliminar'."""
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, *args)
    elif opcion == "eliminar":
        return eliminar_palabra(texto, *args)
    else:
        raise ValueError("Opción no válida. Usa 'contar', 'reemplazar' o 'eliminar'.")


# 38. Genera un programa que nos diga si es de noche, de día o tarde según la
# hora proporcionada por el usuario.
def momento_del_dia(hora):
    """Devuelve 'día' (6-13), 'tarde' (14-20) o 'noche' (21-5)."""
    if not 0 <= hora <= 23:
        raise ValueError("La hora debe estar entre 0 y 23.")
    if 6 <= hora < 14:
        return "día"
    elif 14 <= hora < 21:
        return "tarde"
    else:
        return "noche"


def momento_del_dia_usuario():
    try:
        hora = int(input("Introduce la hora (0-23): "))
        momento = momento_del_dia(hora)
        print("Es por la tarde." if momento == "tarde" else f"Es de {momento}.")
    except ValueError as error:
        print(f"Hora no válida: {error}")


# 39. Escribe un programa que determine qué calificación en texto tiene un
# alumno en base a su calificación numérica. Las reglas de calificación son:
# 0 - 69 insuficiente, 70 - 79 bien, 80 - 89 muy bien, 90 - 100 excelente
def calificacion_texto(nota):
    if not 0 <= nota <= 100:
        raise ValueError("La nota debe estar entre 0 y 100.")
    if nota < 70:
        return "insuficiente"
    elif nota < 80:
        return "bien"
    elif nota < 90:
        return "muy bien"
    else:
        return "excelente"


def calificacion_usuario():
    try:
        nota = float(input("Introduce la calificación (0-100): "))
        print(f"Calificación: {calificacion_texto(nota)}")
    except ValueError as error:
        print(f"Nota no válida: {error}")


# 40. Escribe una función que tome dos parámetros: figura (una cadena que puede
# ser "rectangulo", "circulo" o "triangulo") y datos (una tupla con los datos
# necesarios para calcular el área de la figura).
def calcular_area(figura, datos):
    if figura == "rectangulo":
        base, altura = datos
        return base * altura
    elif figura == "circulo":
        (radio,) = datos
        return math.pi * radio ** 2
    elif figura == "triangulo":
        base, altura = datos
        return base * altura / 2
    else:
        raise ValueError("Figura no válida.")


# 41. Programa que utilice condicionales para determinar el monto final de una
# compra en una tienda en línea, después de aplicar un descuento: pide el
# precio original, pregunta si tiene cupón (sí/no), si lo tiene pide su valor,
# aplica el descuento si es válido (mayor a cero) y muestra el precio final.
def precio_final(precio, cupon=0):
    """Aplica el cupón si es válido; el precio no baja de 0."""
    if cupon > 0:
        return max(precio - cupon, 0)
    return precio


def compra_usuario():
    try:
        precio = float(input("Precio original del artículo: "))
        respuesta = input("¿Tienes un cupón de descuento? (sí/no): ").strip().lower()
        if respuesta in ("sí", "si", "s"):
            cupon = float(input("Valor del cupón: "))
            if cupon > 0:
                print(f"Precio final con descuento: {precio_final(precio, cupon):.2f}€")
            else:
                print(f"Cupón no válido. Precio final: {precio:.2f}€")
        elif respuesta in ("no", "n"):
            print(f"Precio final: {precio:.2f}€")
        else:
            print("Respuesta no reconocida.")
    except ValueError:
        print("Error: introduce un valor numérico.")


def main():
    """Muestra el resultado de cada ejercicio."""
    print("1:", frecuencia_letras("hola mundo"))
    print("2:", doblar_valores([1, 2, 3]))
    print("3:", palabras_que_contienen(["casa", "casamiento", "perro"], "casa"))
    print("4:", diferencia_listas([10, 20, 30], [1, 2, 3]))
    print("5:", evaluar_notas([4, 6, 7]))
    print("6:", factorial(5))
    print("7:", tuplas_a_strings([(1, 2), ("a", "b")]))
    print("9:", filtrar_mascotas(["Perro", "Tigre", "Gato", "Oso"]))
    print("10:", probar_promedio_seguro([2, 4, 6]), probar_promedio_seguro([]))
    print("11:", validar_edad("30"))
    print("12:", longitud_palabras("Hola que tal"))
    print("13:", mayus_minus("abca"))
    print("14:", palabras_que_empiezan_por(["Python", "Java", "PHP"], "p"))
    print("15:", sumar_tres([1, 2, 3]))
    print("16:", palabras_mas_largas("El lenguaje Python es genial", 3))
    print("17:", digitos_a_numero([5, 7, 2]))
    print("18:", estudiantes_destacados)
    print("19:", filtrar_impares([1, 2, 3, 4, 5]))
    print("20:", solo_enteros([1, "a", 2, "b", 3]))
    print("21:", cubo(3))
    print("22:", producto_total([1, 2, 3, 4]))
    print("23:", concatenar_palabras(["Hola", "mundo"]))
    print("24:", diferencia_total([100, 20, 5]))
    print("25:", contar_caracteres("Python"))
    print("26:", resto(10, 3))
    print("27:", promedio([1, 2, 3, 4]))
    print("28:", primer_duplicado([1, 2, 3, 2, 1]))
    print("29:", enmascarar(123456789))
    print("30:", son_anagramas("amor", "roma"))
    buscar_nombre(["Ana", "Luis"], "Ana")
    empleados = [{"nombre": "Ana López", "puesto": "Analista"}]
    print("32:", buscar_puesto("Ana López", empleados), "|", buscar_puesto("Juan Pérez", empleados))
    print("33:", sumar_listas([1, 2, 3], [4, 5, 6]))
    print("34:", caso_uso_arbol())
    print("36: (saldo Alicia, saldo Bob) =", caso_uso_banco())
    texto = "el gato y el perro"
    print("37:", procesar_texto(texto, "contar"))
    print("37:", procesar_texto(texto, "reemplazar", "gato", "loro"))
    print("37:", procesar_texto(texto, "eliminar", "el"))
    print("38:", momento_del_dia(9), momento_del_dia(16), momento_del_dia(23))
    print("39:", calificacion_texto(85))
    print("40:", calcular_area("rectangulo", (4, 5)), round(calcular_area("circulo", (2,)), 2), calcular_area("triangulo", (6, 3)))
    print("41:", precio_final(100, 15))

    if MODO_INTERACTIVO:
        dividir_numeros_usuario()
        pedir_edad()
        buscar_nombre_usuario()
        momento_del_dia_usuario()
        calificacion_usuario()
        compra_usuario()


if __name__ == "__main__":
    main()
