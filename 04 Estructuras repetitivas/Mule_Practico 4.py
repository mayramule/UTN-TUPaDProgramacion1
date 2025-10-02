# Ejercicio 1
# Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 10
# (incluyendo ambos extremos), en orden creciente, mostrando un número por línea
for numero in range(101):
    print(numero)

# Ejercicio 2
# Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
# dígitos que contiene.
numero = int(input("Ingrese un número entero: "))
numero = abs(numero)
contador = 0
if numero == 0:
    contador = 1
else:
    while numero > 0:
        numero = numero // 10  
        contador += 1
print("La cantidad de dígitos es:", contador)

# Ejercicio 3
# Escribe un programa que sume todos los números enteros comprendidos entre dos valores
# dados por el usuario, excluyendo esos dos valores.
inicio = int(input("Ingrese el primer número: "))
fin = int(input("Ingrese el segundo número: "))
suma = 0
for i in range(inicio + 1, fin):
    suma += i
print("La suma es:", suma)

# Ejercicio 4
# Elabora un programa que permita al usuario ingresar números enteros y los sume en
# secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
# un 0.
total = 0
numero = int(input("Ingrese un número o 0 para detenerse: "))
while numero != 0:
    total += numero
    numero = int(input("Ingrese un número o 0 para detenerse: "))
print("El total acumulado es:", total)

# Ejercicio 5
# Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
# programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
numero_secreto = random.randint(0, 9)
intentos = 0
intento = -1
while intento != numero_secreto:
    intento = int(input("Adivina el número (0-9): "))
    intentos += 1
print("¡Correcto! Número de intentos:", intentos)

# Ejercicio 6
# Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
# entre 0 y 100, en orden decreciente.
for numero in range(100, -1, -1):
    if numero % 2 == 0:
        print(numero)

# Ejercicio 7
# Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
# número entero positivo indicado por el usuario
n = int(input("Ingrese un número: "))
suma = 0
for i in range(n + 1):
    suma += i
print("La suma es:", suma)

# Ejercicio 8
# Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
# programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
# negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
# menor, pero debe estar preparado para procesar 100 números con un solo cambio).
pares = 0
impares = 0
positivos = 0
negativos = 0
cantidad = 100
i = 0

while i < cantidad:
    numero = int(input("Ingrese un número: "))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1
    i += 1

print("Pares:", pares)
print("Impares:", impares)
print("Positivos:", positivos)
print("Negativos:", negativos)

# Ejercicio 9
# Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
# media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
# poder procesar 100 números cambiando solo un valor).
suma = 0
cantidad = 100
for i in range(cantidad):
    numero = int(input("Ingrese un número entero: "))
    suma += numero
media = suma / cantidad
print("La media es:", media)

# Ejercicio 10
# Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.
numero = int(input("Ingrese un número: "))
invertido = 0

while numero > 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero = numero // 10

print("Número invertido:", invertido)
