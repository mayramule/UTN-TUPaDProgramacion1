'''1) Dado el diccionario precios_frutas'''
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
'''Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300'''

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print("Despues de añadir las frutas:")
print(precios_frutas)

'''2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800'''

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print("Después de actualizar los precios:")
print(precios_frutas)

'''3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios.'''

lista_frutas = list(precios_frutas.keys())

print("Lista de las frutas:")
print(lista_frutas)

'''4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe.'''
print("Por favor, ingrese los contactos y sus numeros.")
agenda = {}
MAX_CONTACTOS = 5

for i in range(MAX_CONTACTOS):
    print(f"Contacto {i + 1} de {MAX_CONTACTOS}:")
    nombre = input("Ingrese el nombre del contacto: ").strip().lower()
    numero = input("Ingrese el número de teléfono: ").strip() 
    agenda[nombre] = numero
print("--- CARGA FINALIZADA ---")
print("Agenda actual:", agenda)

while True:
    print("---OPCIONES---:")
    print("1. Consultar número de teléfono")
    print("2. Salir del programa")
    
    opcion = input("Elija una opción (1 o 2): ")
    
    if opcion == '1':
        nombre_consulta = input("Ingrese el nombre del contacto a buscar: ").strip()
        nombre_normalizado_consulta = nombre_consulta.lower()
        numero_encontrado = agenda.get(nombre_normalizado_consulta)

        if numero_encontrado:
            print(f"El número de teléfono de {nombre_consulta} es: {numero_encontrado}")
        else:
            print(f"Error: El contacto '{nombre_consulta}' no se encuentra en la agenda.")
            
    elif opcion == '2':
        print("Saliendo del programa...")
        break
        
    else:
        print("Opción no válida. Por favor, elija 1 o 2.")

'''6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno.'''
alumnos = {
    "Mayra": (10, 9, 8),
    "Felipe": (6, 7, 7),
    "Natalia": (9, 9, 10)
}

print(alumnos)

for nombre, notas in alumnos.items():
    suma_notas = sum(notas)
    cantidad_notas = len(notas)
    promedio = suma_notas / cantidad_notas
    
    print(f"Alumno: {nombre}")
    print(f"  Notas: {notas}")
    print(f"  Promedio: {round(promedio, 2)}")

'''7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir).'''

aprobados_parcial1 = {1, 5, 10, 2, 12, 15}
aprobados_parcial2 = {1,2, 11, 13, 14, 5}

print(f"Aprobaron Parcial 1: {aprobados_parcial1}")
print(f"Aprobaron Parcial 2: {aprobados_parcial2}")

ambos_parciales = aprobados_parcial1 & aprobados_parcial2

print("Estudiantes que aprobaron ambos Parciales:")
print(ambos_parciales)

al_menos_uno = aprobados_parcial1 | aprobados_parcial2
print("Estudiantes que aprobaron al menos un parcial:")
print(al_menos_uno)

solo_uno = aprobados_parcial1 ^ aprobados_parcial2
print("Estudiantes que aprobaron solo uno de los dos parciales:")
print(solo_uno)

'''8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe.'''

stock_productos = {
    "Laptop": 15,
    "Mouse": 50,
    "Teclado": 30,
    "Monitor": 10
}

print("--- SISTEMA DE GESTIÓN DE STOCK ---")
print("Inventario inicial:", stock_productos)

while True:
    print("1. Consultar Stock de un producto")
    print("2. Modificar/Agregar Stock")
    print("3. Salir")
    
    opcion = input("Elija una opción (1, 2 o 3): ")
    
    if opcion == '1':
        nombre_producto = input("Ingrese el nombre del producto a consultar: ").strip()
        stock = stock_productos.get(nombre_producto)
        
        if stock is not None:
            print(f"STOCK de {nombre_producto}: {stock} unidades.")
        else:
            print(f"El producto '{nombre_producto}' no se encuentra en el inventario.")

    elif opcion == '2':
        nombre_producto = input("Ingrese el nombre del producto a modificar/agregar: ").strip()
        try:
            cantidad_agregar = int(input("Ingrese la cantidad de unidades a sumar (ej: 5) o restar (ej: -2): "))
        except ValueError:
            print("Entrada no válida. Debe ingresar un número entero.")
            continue
            
        if nombre_producto in stock_productos:
            stock_actual = stock_productos[nombre_producto]
            stock_productos[nombre_producto] = stock_actual + cantidad_agregar
            print(f"Stock de {nombre_producto} actualizado. Nuevo stock: {stock_productos[nombre_producto]}.")
        else:
            stock_productos[nombre_producto] = cantidad_agregar
            print(f"➕ Producto '{nombre_producto}' agregado con stock inicial de {cantidad_agregar} unidades.")
            
    elif opcion == '3':
        print("Saliendo del sistema:")
        print(stock_productos)
        break
        
    else:
        print("Opción no válida. Por favor, ingrese 1, 2 o 3.")

'''9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
Permití consultar qué actividad hay en cierto día y hora.'''

# 1. Crear el diccionario 'agenda' donde las claves son tuplas (dia, hora)
agenda = {
    ("lunes", "10:00"): "Reunión de planificación",
    ("martes", "15:00"): "Clase de inglés",
    ("miércoles", "09:30"): "Entrenamiento en el gimnasio",
    ("viernes", "18:00"): "Revisión de código"
}

print("--- AGENDA DE EVENTOS SEMANAL ---")
print(agenda)
print("--- CONSULTA DE EVENTO ---")
dia_consulta = input("Ingrese el día (ej: lunes): ").strip().lower()
hora_consulta = input("Ingrese la hora (formato HH:MM, ej: 10:00): ").strip()

clave_consulta = (dia_consulta, hora_consulta)

evento = agenda.get(clave_consulta)

if evento:
    print(f"Evento en {clave_consulta[0]} a las {clave_consulta[1]}:")
    print(f"   -> {evento}")
else:
    print(f"No hay evento programado para el día {clave_consulta[0]} a las {clave_consulta[1]}.")

'''10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores.'''

paises_capitales = {
    "Argentina": "Buenos Aires",
    "Chile": "Santiago",
    "Uruguay": "Montevideo",
    "España": "Madrid",
    "Perú": "Lima"
}

print("--- DICCIONARIO (País: Capital) ---")
print(paises_capitales)
capitales_paises = {}

for pais in paises_capitales:
    capital = paises_capitales[pais] 
    capitales_paises[capital] = pais
    
    
print("--- DICCIONARIO (Capital: País) ---")
print(capitales_paises)