import csv 

# FUNCIONES DE ENTRADA Y VISUALIZACION

def validar_entrada_numero(mensaje):
    '''Pide un valor al usuario y se asegura de que sea un número entero positivo o cero.'''

    while True:
        entrada = input(mensaje).strip()
        
        if len(entrada) == 0:
            print("Entrada vacía. Necesitas ingresar un número.")
            continue 

        if entrada.isdigit():
            numero = int(entrada)
            
            if numero < 0:
                print("El número ingresado debe ser positivo.")
                continue 
                
            return numero  
        else:
            print("ERROR: Por favor ingrese solo números enteros positivos.")
            continue 


def mostrar_resultados(lista_paises):
    '''Muestra la lista de países en un formato de tabla. Los números grandes están separados por puntos.'''

    if len(lista_paises) == 0: 
        print("\n No se encontraron resultados que coincidan con la búsqueda.")
        return 

    print("\n   RESULTADOS ")
    print(f"{'Nombre':<25} | {'Población':>15} | {'Superficie (km²)':>20} | {'Continente':<15}")
    print("-" * 78)
    
    for pais in lista_paises:
        # Pone puntos para separar miles en los numeros grandes
        poblacion_puntos = f"{pais['poblacion']:,}".replace(",", ".")
        superficie_puntos = f"{pais['superficie']:,}".replace(",", ".")
        
        print(
            f"{pais['nombre']:<25} | "
            f"{poblacion_puntos:>15} | "
            f"{superficie_puntos:>20} | "
            f"{pais['continente']:<15}"
        )
    print(f"\n   Total de registros mostrados: {len(lista_paises)}")



# FUNCIONES DE CARGA DE DATOS

def cargar_datos_csv(nombre_archivo):
    '''Lee los datos desde el archivo CSV y los carga en el programa. Incluye manejo de errores si el archivo falta o si los datos dentro son invalidos.'''
    paises = [] 
    try:
        print("Cargando archivo...")
        
        paises_temp = []
        
        with open(nombre_archivo, 'r', newline='', encoding='utf-8') as archivo: 
            lector_csv = csv.reader(archivo, delimiter=',') 
            next(lector_csv)  # Salta la primera fila que contiene los encabezados.
            
            for fila in lector_csv:
                if len(fila) == 4: # Verifica que la fila contenga 4 columnas.
                    nombre, poblacion_str, superficie_str, continente = fila
                    
                    if poblacion_str.strip().isdigit() and superficie_str.strip().isdigit():
                        poblacion = int(poblacion_str.strip())
                        superficie = int(superficie_str.strip())
                        
                        pais = {
                            "nombre": nombre.strip(),
                            "poblacion": poblacion,
                            "superficie": superficie,
                            "continente": continente.strip()
                        }
                        paises_temp.append(pais)
                    else:
                        print(f"ATENCIÓN: '{nombre}' tiene datos incorrectos. Registro omitido.")
                        continue
        
        paises = paises_temp
        print(f" Se cargaron {len(paises)} países exitosamente.")
        return paises 
        
    except Exception:
        # Captura errores de Archivo No Encontrado o de lectura.
        print(f"ADVERTENCIA: Falló la lectura del archivo '{nombre_archivo}'.")
        
    if len(paises) == 0:
        print("ERROR CRÍTICO: El archivo no se pudo leer o no existe.")

    return []


# FUNCIONES DE BUSCAR Y FILTRAR

def mostrar_menu_filtros():
    """Imprime un submenú para buscar y filtar."""
    print("\n" + "╔═════════════════════════════════════╗")
    print("║      SUBMENU: BUSCAR Y FILTAR       ║")
    print("╠═════════════════════════════════════╣")
    print("║ 1. Buscar por Nombre                ║")
    print("║ 2. Filtrar por Continente           ║")
    print("║ 3. Filtrar por Población            ║")
    print("║ 4. Filtrar por Superficie           ║")
    print("║ 5. Volver                           ║")
    print("╚═════════════════════════════════════╝")

def buscar_por_nombre(lista_paises, nombre_buscado):
    '''Busca paises cuyo nombre incluya la palabra clave introducida. No hay diferencia si usa mayusculas o minusculas.'''

    nombre_buscado_lower = nombre_buscado.lower() 
    resultados = []
    for pais in lista_paises:
        if nombre_buscado_lower in pais['nombre'].lower():
            resultados.append(pais)
    return resultados

def filtrar_por_continente(lista_paises, continente_buscado):
    '''Filtra la lista para mostrar solo los países que pertenecen al continente especificado. No hay diferencia si usa mayusculas o minusculas.'''

    continente_buscado_lower = continente_buscado.lower() 
    resultados = []
    for pais in lista_paises:
        if pais['continente'].lower() == continente_buscado_lower:
            resultados.append(pais)
    return resultados

def filtrar_por_rango(lista_paises, clave, valor_min, valor_max):
    '''Filtra países donde el valor de la clave se encuentra entre el minimo y el miximo indicado.'''
    
    if valor_min > valor_max:
        print("ERROR: El valor mínimo no puede ser mayor que el máximo.")
        return []
    
    resultados = []
    for pais in lista_paises:
        valor = pais[clave]
        if valor_min <= valor <= valor_max:
            resultados.append(pais)
            
    return resultados

def ejecutar_filtros(paises):
    '''Controla el flujo del submenú.'''
    while True:
        mostrar_menu_filtros()
        opcion_filtro = input("Ingrese una opción por favor (1-5): ").strip()
        
        resultados = []
        mostrar = True
        
        match opcion_filtro:
            case '1':
                busqueda = input("Ingrese el nombre del país: ").strip()
                resultados = buscar_por_nombre(paises, busqueda)
                
            case '2':
                continente = input("Ingrese el Continente: ").strip()
                resultados = filtrar_por_continente(paises, continente)

            case '3':
                rango_min = validar_entrada_numero("Población Mínima: ")
                rango_max = validar_entrada_numero("Población Máxima: ")
                
                resultados = filtrar_por_rango(paises, 'poblacion', rango_min, rango_max)
                
            case '4':
                rango_min = validar_entrada_numero("Superficie Mínima (km²): ")
                rango_max = validar_entrada_numero("Superficie Máxima (km²): ")
                
                resultados = filtrar_por_rango(paises, 'superficie', rango_min, rango_max)
                
            case '5':
                print("Volviendo al Menú Principal...")
                return
            
            case _:
                print("Opción no válida. Intente de nuevo.")
                mostrar = False
                
        if mostrar:
            mostrar_resultados(resultados)


# FUNCIONES PARA ORDENAR DATOS POR NOMBRE, POBLACION Y SUPERFICIE 

def mostrar_menu_ordenamiento():
    '''Imprime el submenú.'''
    print("\n" + "╔═══════════════════════════════════════╗")
    print("║   SUBMENU: ORDENAR DATOS              ║")
    print("╠═══════════════════════════════════════╣")
    print("║ 1. Por Nombre (A-Z)                   ║")
    print("║ 2. Por Población (Mayor a Menor)      ║")
    print("║ 3. Por Superficie (Menor a Mayor)     ║")
    print("║ 4. Volver                             ║")
    print("╚═══════════════════════════════════════╝")

def ordenar_paises(lista_paises, clave, reverso):
    '''Organiza la lista de países de forma ascendente o descendente según la clave especificada.'''

    lista_ordenada = lista_paises[:] 
    cantidad = len(lista_ordenada)

    for i in range(cantidad - 1):
        for j in range(0, cantidad - i - 1):
            
            valor_actual = lista_ordenada[j][clave]
            valor_siguiente = lista_ordenada[j + 1][clave]

            hay_que_intercambiar = False
            
            if reverso == True:
                if valor_actual < valor_siguiente:
                    hay_que_intercambiar = True
            else:
                if valor_actual > valor_siguiente:
                    hay_que_intercambiar = True

            if hay_que_intercambiar == True:
                lista_ordenada[j], lista_ordenada[j + 1] = lista_ordenada[j + 1], lista_ordenada[j]

    return lista_ordenada

def ejecutar_ordenamiento(paises):
    '''Controla el flujo del submenú.'''

    while True:
        mostrar_menu_ordenamiento()
        opcion = input("Ingrese una opción por favor (1-4): ").strip()
        
        lista_ordenada = []
        
        match opcion:
            case '1':
                lista_ordenada = ordenar_paises(paises, 'nombre', reverso=False)
                print("\n Países ordenados por Nombre (A-Z):")
            case '2':
                lista_ordenada = ordenar_paises(paises, 'poblacion', reverso=True)
                print("\n Países ordenados por Población (Mayor a Menor):")
            case '3':
                lista_ordenada = ordenar_paises(paises, 'superficie', reverso=False)
                print("\n Países ordenados por Superficie (Menor a Mayor):")
            case '4':
                print("Volviendo al Menú Principal...")
                return
            case _:
                print("Opción no válida. Intente de nuevo.")
                continue
            
        mostrar_resultados(lista_ordenada)


# FUNCIONES DE ESTADÍSTICAS


def calcular_max_min_poblacion(lista_paises):
    '''Encuentra el país (diccionario completo) con mayor y menor población.'''

    pais_max = lista_paises[0]
    pais_min = lista_paises[0]

    for pais in lista_paises:
        if pais['poblacion'] > pais_max['poblacion']:
            pais_max = pais
        if pais['poblacion'] < pais_min['poblacion']:
            pais_min = pais
            
    return pais_max, pais_min

def calcular_promedios(lista_paises):
    '''Calcula el promedio de la población y la superficie de todos los países.'''

    if len(lista_paises) == 0:
        return 0, 0
    
    total_poblacion = 0
    total_superficie = 0
    
    for pais in lista_paises:
        total_poblacion += pais['poblacion']
        total_superficie += pais['superficie']
        
    cantidad = len(lista_paises)
    promedio_poblacion = total_poblacion / cantidad
    promedio_superficie = total_superficie / cantidad
    
    return promedio_poblacion, promedio_superficie

def contar_por_continente(lista_paises):
    '''Cuenta cuántos países hay en cada continente y devuelve un resumen.'''

    conteo = {}
    for pais in lista_paises:
        continente = pais['continente']
        if continente in conteo:
            conteo[continente] += 1
        else:
            conteo[continente] = 1 
    return conteo

def ejecutar_estadisticas(paises):
    '''Muestra un resumen de los indicadores estadísticos.'''
    
    if len(paises) == 0:
        print("No hay datos cargados para generar estadísticas.")
        return

    
    print("\n  RESULTADOS ESTADÍSTICOS")
    
    
    # Países con Máx/Mín Población
    max_p, min_p = calcular_max_min_poblacion(paises)
    
    print("\n  País con Mayor y Menor Población ")
    print(f"\n   MAYOR Población: {max_p['nombre']} ({max_p['poblacion']:,d} hab.)".replace(",", "."))
    print(f"   MENOR Población: {min_p['nombre']} ({min_p['poblacion']:,d} hab.)".replace(",", "."))
    
    # Promedios
    prom_pobl, prom_sup = calcular_promedios(paises)
    print("\n  Promedios ")
    
# Mostramos solo dos decimales para que los promedios sean más fáciles de leer.
    print(f"\n   Promedio de Población: {prom_pobl:.2f} habitantes")
    print(f"   Promedio de Superficie: {prom_sup:.2f} km²")
    
    # Conteo por Continente
    conteo_cont = contar_por_continente(paises)
    print("\n  Conteo por Continente ")
    for continente, cantidad in conteo_cont.items():
        print(f"   {continente}: {cantidad} países")

'''
# 6. FUNCIÓN PARA AGREGAR PAÍS (Extra)
def agregar_nuevo_pais(paises):
    """
    Pide los datos de un nuevo país, valida que la información sea correcta y lo añade a la lista de países cargados.
    """
    print("\n   AGREGAR UN NUEVO PAÍS")
    
    # Solicitar y validar que el nombre no este vacio
    nombre = input("Ingrese el nombre del país: ").strip()
    if nombre == "":
        print("Operación cancelada. El nombre no puede estar vacío.")
        return

    # Solicitar y validar que ingrese un numero para poblacion
    poblacion = validar_entrada_numero("Ingrese la cantidad de población: ")
    
    #Solicitar y validar que ingrese un numero para validad la superficie 
    superficie = validar_entrada_numero("Ingrese la cantidad de Superficie en km²: ")
    
    #Solicitar y validar que el continente no este vacio
    continente = input("Ingrese el Continente: ").strip()
    if continente == "":
        print("Operación cancelada. El Continente no puede estar vacío.")
        return
    
    #Crear el nuevo diccionario
    nuevo_pais = {
        "nombre": nombre,
        "poblacion": poblacion,
        "superficie": superficie,
        "continente": continente
    }
    
    #Agregar a la lista
    paises.append(nuevo_pais)
    
    print(f"\n El país '{nombre}' ha sido agregado con éxito a la lista.")
    print(f"Total de países cargados: {len(paises)}")


# 7. FUNCIÓN PARA GUARDAR DATOS EN CSV (Extra)

def guardar_datos_csv(paises, nombre_archivo):
    """Reescribe la lista completa de países en el archivo CSV."""
    try:
        # Abrimos el archivo en modo escritura ('w') para reescribir lo que queremos guardar.
        with open(nombre_archivo, 'w', newline='', encoding='utf-8') as archivo:
            escritor_csv = csv.writer(archivo, delimiter=',')
            escritor_csv.writerow(['nombre', 'poblacion', 'superficie', 'continente'])
           
            for pais in paises:
                escritor_csv.writerow([
                    pais['nombre'],
                    pais['poblacion'],
                    pais['superficie'],
                    pais['continente']
                ])
        
        print(f"\n ¡Éxito! Se guardaron {len(paises)} registros en '{nombre_archivo}'.")
        return True
    
    except Exception:
        print("\n ERROR DE ESCRITURA: No se pudo guardar el archivo.")
        return False
'''

# FUNCIONES DEL MAIN

def mostrar_menu():
    '''Imprime el menú de opciones principal de la aplicación.'''
    #Aca podria poner al menu lo de agergar pais y guardar esos cambios

    print("\n" + "╔═══════════════════════════════════════╗")
    print("║  GESTOR DE DATOS DE PAÍSES - MENÚ     ║")
    print("╠═══════════════════════════════════════╣")
    print("║ 1. Buscar y filtrar                   ║")
    print("║ 2. Ordenar                            ║")
    print("║ 3. Estadísticas                       ║")
    #print("║ 4. Agregar País                       ║")
    #print("║ 5. Guardar Cambios en CSV             ║")
    print("║ 4. Salir                              ║")
    print("╚═══════════════════════════════════════╝")

def main():
   
    '''Función principal que inicia la carga de datos y controla el bucle de la aplicación.'''

    nombre_archivo_csv = "paises.csv" 
    paises = cargar_datos_csv(nombre_archivo_csv)
    
    if len(paises) == 0: 
        print(" El programa ha finalizado debido a un error de carga crítica.")
        return

    while True:
        mostrar_menu()
        opcion = input("\n   Ingrese una opción por favor (1-4): ").strip()
        
        match opcion:
            case '1':
                ejecutar_filtros(paises)
            case '2':
                ejecutar_ordenamiento(paises)
            case '3':
                ejecutar_estadisticas(paises)
            #case '4': 
                #agregar_nuevo_pais(paises)
            #case '5':
                    #Opción de Guardado Manual
                #guardar_datos_csv(paises, nombre_archivo_csv)
            #case '6':
                # Opción de Salida con pregunta de Guardado
                #print("\n ¿Desea guardar los cambios realizados antes de salir? (s/n)")
                #respuesta = input("Respuesta: ").lower().strip()
                #if respuesta == 's':
                    #guardar_datos_csv(paises, nombre_archivo_csv)
            case '4':
                print("\n ¡Gracias por usar el Gestor de Datos! Saliendo del programa...")
                break
            case _:
                print("\n Opción no válida. Por favor, ingrese un número del 1 al 4.")

if __name__ == "__main__":
    main()