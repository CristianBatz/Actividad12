def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    menores = [x for x in lista[1:] if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista[1:] if x > pivote]

    return quick_sort(menores) + iguales + quick_sort(mayores)


def busqueda_de_valor(lista, objetivo):
    for elemento in lista:
        return elemento
    return None


mensajeria = {}
print("===Registro de mensajeria ===")
cantidad = int(input("Ingrese la cantidad de repartidores que participaron: "))
for i in range(cantidad):
    print(f"Repartidor #{i + 1}")
    mensajeria_nombre = input("Ingrese el nombre del repartidor: ")
    paquetes_cantidad = int(input("Ingrese la cantidad de paquetes: "))
    zona = input("Ingrese la zona del repartido: ")
    mensajeria[mensajeria_nombre] = {
        "paquetes_cantidad": paquetes_cantidad,
        "zona": zona
    }
repartidores = list(mensajeria.items())
print("=== Registro original ===")
for nombre, valor in mensajeria.items():
    print("nombre: ", nombre)
    print("paquetes: ", valor["paquetes_cantidad"])
    print("zona: ", valor["zona"])

print("=== Ranking ===")
resultado = quick_sort(repartidores)
for nombre, valor in resultado:
    print(f"nombre: {nombre}, paquetes: {valor['paquetes_cantidad']}, zona: {valor['zona']}")

print("=== Busqueda ===")
buscar_nombre = input("Ingrese el nombre: ")
resultadoA = busqueda_de_valor(resultado, buscar_nombre)
if resultadoA is not None:
        print(f"{resultadoA}")
else:
    print("No se ha encontrado el resultado")
