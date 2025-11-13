'''1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario'''

def factorial_recursivo(n):
    if n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

def mostrar_factoriales():
    try:
        num_usuario = int(input("Ingrese un numero entero positivo: "))
        if num_usuario < 0:
            print("Por favor, ingrese un numero no negativo.")
            return

        print(f"Factoriales desde 1 hasta {num_usuario}:")
        for i in range(1, num_usuario + 1):
            resultado = factorial_recursivo(i)
            print(f"{i}! = {resultado}")

    except ValueError:
        print("Entrada no valida. Por favor, ingrese un numero entero.")

'''2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique.'''

def fibonacci(n):
    if n == 0:  
        return 0
    elif n == 1: 
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2) 
    
def mostrar_fibonacci():
    num = int(input("Ingrese un numero: "))
    for i in range(num):
        print(f"F({i}) = {fibonacci(i)}")

mostrar_fibonacci()

'''3) Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula 𝑛
𝑚 = 𝑛 ∗ 𝑛
(𝑚−1). Prueba esta función en un algoritmo general.'''

def potencia(base, exponente):
    if exponente == 0: 
        return 1
    else:
        return base * potencia(base, exponente - 1)  

def mostrar_potencia():
    base = int(input("Ingrese la base: "))
    exponente = int(input("Ingrese el exponente: "))
    print(f"{base}^{exponente} = {potencia(base, exponente)}")

mostrar_potencia()

'''4) Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto.
Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y
unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este
procedimiento:
1. Dividir el número por 2.
2. Guardar el resto (0 o 1).
3. Repetir el proceso con el cociente hasta que llegue a 0.
4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.'''

def decimal_a_binario_recursivo(num_decimal):
    if num_decimal == 0:
        return ""
    else:
        cociente = num_decimal // 2
        resto = num_decimal % 2
        return decimal_a_binario_recursivo(cociente) + str(resto)

def probar_binario():
    num = 10
    resultado = decimal_a_binario_recursivo(num)
    print(f"\nEl número {num} en binario es: {resultado}") 



'''5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no lo es.
Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed().'''

def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False 

palabra = input("Ingrese una palabra: ").lower()
print(es_palindromo(palabra))  

'''6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.
Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.'''

def suma_digitos_recursiva(n):
    if n == 0:
        return 0
    else:
        ultimo_digito = n % 10
        resto_del_numero = n // 10
        return ultimo_digito + suma_digitos_recursiva(resto_del_numero)

def probar_suma_digitos():
    print(f"\nSuma de dígitos de 1234: {suma_digitos_recursiva(1234)}") 
    print(f"Suma de dígitos de 305: {suma_digitos_recursiva(305)}")   

'''7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide.'''

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

print(contar_bloques(1)) 
print(contar_bloques(2))  
print(contar_bloques(4))  

'''8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.'''

def contar_digito_recursivo(numero, digito):
    if numero == 0:
        return 0

    ultimo_digito = numero % 10
    resto_del_numero = numero // 10

    if ultimo_digito == digito:
        return 1 + contar_digito_recursivo(resto_del_numero, digito)
    else:
        return 0 + contar_digito_recursivo(resto_del_numero, digito)

def probar_contar_digito():
    print(f"\nVeces que aparece el dígito 2 en 12233421: {contar_digito_recursivo(12233421, 2)}") 
    print(f"Veces que aparece el dígito 7 en 123456: {contar_digito_recursivo(123456, 7)}") 

