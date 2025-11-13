# Ejercicio 1
# Imprime "Hola Mundo!" en pantalla
print("Hola Mundo!")


# Ejercicio 2
# Pide el nombre al usuario y lo muestra en un saludo
nombre = input("Por favor, ingrese su nombre: ")
print(f"Hola {nombre}!")


# Ejercicio 3
# Pide nombre, apellido, edad y lugar de residencia y lo imprime en una frase
nombre = input("Por favor, ingrese su nombre: ")
apellido = input("Por favor, ingrese su apellido: ")
edad = input("Por favor, ingrese su edad: ")
lugar_residencia = input("Por favor, ingrese su lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar_residencia}.")


# Ejercicio 4
# Pide el radio de un círculo y calcula área y perímetro
import math
radio_circulo = float(input("Por favor, ingrese el radio del círculo: "))
area_circulo = round(math.pi * (radio_circulo**2), 2)
perimetro_circulo = round(2 * math.pi * radio_circulo, 2)
print(f"El área del círculo es de {area_circulo} y el perímetro es de {perimetro_circulo}.")


# Ejercicio 5
# Convierte segundos a horas
cantidad_segundos = float(input("Por favor, ingrese la cantidad de segundos a convertir: "))
horas = round(cantidad_segundos / 3600, 2)
print(f"{cantidad_segundos} segundos equivalen a {horas} horas.")


# Ejercicio 6
# Tabla de multiplicar
numero_a_multiplicar = int(input("Por favor, ingrese un número entero: "))
print(f"""
{numero_a_multiplicar} x 0 = {numero_a_multiplicar * 0}
{numero_a_multiplicar} x 1 = {numero_a_multiplicar * 1}
{numero_a_multiplicar} x 2 = {numero_a_multiplicar * 2}
{numero_a_multiplicar} x 3 = {numero_a_multiplicar * 3}
{numero_a_multiplicar} x 4 = {numero_a_multiplicar * 4}
{numero_a_multiplicar} x 5 = {numero_a_multiplicar * 5}
{numero_a_multiplicar} x 6 = {numero_a_multiplicar * 6}
{numero_a_multiplicar} x 7 = {numero_a_multiplicar * 7}
{numero_a_multiplicar} x 8 = {numero_a_multiplicar * 8}
{numero_a_multiplicar} x 9 = {numero_a_multiplicar * 9}
""")


# Ejercicio 7
# Operaciones con dos números
numero_a = float(input("Por favor, ingrese un número distinto de 0: "))
numero_b = float(input("Por favor, ingrese otro número distinto de 0: "))
suma = numero_a + numero_b
resta = numero_a - numero_b
multiplicacion = numero_a * numero_b
division = round(numero_a / numero_b, 2)
print(f"""
Resultado de la suma: {suma}
Resultado de la resta: {resta}
Resultado de la multiplicación: {multiplicacion}
Resultado de la división: {division}
""")


# Ejercicio 8
# Índice de masa corporal
peso = float(input("Por favor, ingrese su peso en kg: "))
altura = float(input("Por favor, ingrese su altura en metros: "))
imc = round(peso / (altura**2), 2)
print(f"Su índice de masa corporal es {imc}")


# Ejercicio 9
# Conversión Celsius a Fahrenheit
celsius = float(input("Por favor, ingrese una temperatura en °C: "))
fahrenheit = round((9/5) * celsius + 32, 2)
print(f"{celsius}°C equivalen a {fahrenheit}°F")


# Ejercicio 10
# Promedio de 3 números
numero_a = float(input("Por favor, ingrese el primer número: "))
numero_b = float(input("Por favor, ingrese el segundo número: "))
numero_c = float(input("Por favor, ingrese el tercer número: "))
promedio = round((numero_a + numero_b + numero_c) / 3, 2)
print(f"El promedio de los números ingresados es {promedio}.")