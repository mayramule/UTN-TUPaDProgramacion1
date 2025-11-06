
productos = []

with open("productos.txt", "r") as archivo:
    print("--- PRODUCTOS ACTUALES ---")
    for linea in archivo:
        linea = linea.strip()
        nombre, precio, cantidad = linea.split(",")
        producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
        productos.append(producto)
        print(f"Producto:{nombre} | Precio:${precio} | Cantidad:{cantidad}")

while True:
    print("¿Queres agregar un producto nuevo?")
    opcion = input("Escribe s para si o n para no: ").lower()
    if opcion == "n":
        break

    nombre = input("Nombre del producto: ")
    precio = input("Precio del producto: ")
    cantidad = input("Cantidad: ")

    nuevo_producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    productos.append(nuevo_producto)
    print("Producto agregado correctamente.")

with open("productos.txt", "w") as archivo:
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print("Archivo actualizado correctamente.\n")

print("--- PRODUCTOS ACTUALES ---")
for p in productos:
    print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")


