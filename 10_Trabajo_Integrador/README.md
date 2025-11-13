# GESTOR DE DATOS DE PAÍSES 

**TECNICATURA UNIVERSITARIA EN PROGRAMACIÓN (A DISTANCIA)**
**Materia:** Programación 1

---

## ✨ Tabla de contenidos

* [1. Objetivo del Proyecto](#-1-objetivo-del-proyecto)
* [2. Descripción del Programa](#-2-descripción-del-programa)
* [3. Funcionalidades Clave](#-3-funcionalidades-clave)
* [4. Instrucciones de Uso](#-4-instrucciones-de-uso)
* [5. Ejemplos de Entradas y Salidas](#-5-ejemplos-de-entradas-y-salidas)
* [6. Participación de la Integrante](#-6-participación-de-la-integrante)

---

## 1. Objetivo del Proyecto 🎯

El desarrollo de esta aplicación busca **afianzar el uso de estructuras de datos, modularización con funciones y técnicas de filtrado/ordenamiento**, aplicando los conceptos aprendidos en Programación 1.

* **Alcance:** Desarrollar una aplicación en Python que permita gestionar información sobre países, aplicando listas, diccionarios, funciones, estructuras condicionales y repetitivas, ordenamientos y estadísticas.
* **Requisito de Datos:** El sistema debe ser capaz de leer datos desde un archivo CSV, realizar consultas y generar indicadores clave a partir del dataset.

---

## 2. Descripción del Programa 💻

Esta es una aplicación de **consola** desarrollada en **Python 3** que opera sobre un conjunto de datos geográficos y demográficos de países, cargados desde el archivo `paises.csv`.

El programa aplica los conceptos fundamentales de **modularización** (uso de funciones) y **estructuras de datos** (**Listas de Diccionarios**) para transformar los datos brutos en una herramienta de consulta interactiva.

---

## 3. Funcionalidades Clave 🛠️

| Categoría | Funcionalidad | Descripción |
| :---: | :--- | :--- |
| **🔎 Búsqueda** | Por Nombre | Búsqueda parcial o exacta. **No hay diferencia si usa mayusculas o minusculas.** |
| **🔧 Filtros** | Por Continente, Población o Superficie | Filtra por continente exacto o por rangos numéricos de Población y Superficie. |
| **↕ Ordenamiento**| Por Nombre, Población o Superficie | Permite ordenar la lista de países por el criterio deseado (Ascendente/Descendente). |
| **📊 Estadísticas**| Promedios, Máx/Mín y Conteo | Calcula la población/superficie promedio, el país más/menos poblado y el total de países por continente. |
| **✅ Validación**| Entradas numéricas | Asegura que el usuario ingrese números enteros positivos donde se requieren rangos u opciones. |

---

## 4. Instrucciones de Uso ⚙️

### Ubicación y Ejecución

1.  Asegúrese de que el archivo del código (`T_integrador_MuleMayra.py`) y el archivo de datos (`paises.csv`) estén en la **misma carpeta**.
2.  Abra la terminal (CMD, PowerShell o Bash) en esa carpeta.
3.  Ejecute la aplicación con el siguiente comando:

    ```bash
    python T_integrador_MuleMayra.py
    ```
4.  El programa iniciará el menú principal. Simplemente ingrese el número correspondiente a la acción que desee ejecutar.

### 📄 Formato del CSV (Requisitos)

El archivo de datos debe tener los siguientes encabezados, con datos separados por comas:

| Columna | Tipo de Dato | Requisito |
| :--- | :--- | :--- |
| `nombre` | Texto (string) | Nombre del país. |
| `poblacion` | Número entero | Mayor o igual a cero. |
| `superficie` | Número entero | Mayor a cero. |
| `continente` | Texto (string) | Nombre del continente. |

---

## 5. Ejemplos de Entradas y Salidas 🧪

| Ejemplo | Acción | Entrada de Usuario | Salida Clave |
| :---: | :--- | :--- | :--- |
| **1** | Búsqueda parcial | Menú 1, Opción 1. Nombre: `arg` | Muestra el registro completo de Argentina. |
| **2** | Filtro por rango | Menú 1, Opción 3. Min: `50000000`, Máx: `300000000` | Lista de países en ese rango de población. |
| **3** | Manejo de Error | Población mínima: `abc` | `[ERROR] Por favor ingrese solo números enteros positivos.` |
| **4** | Salida | Menú Principal: `4` | `¡Gracias por usar el Gestor de Datos! Saliendo del programa...` |

---

## 6. Participación de la Integrante 🧑‍💻

| Rol | Nombre |
| :--- | :--- |
| **Alumno Desarrollador** | Mulé Mayra |