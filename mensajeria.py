def quick_sort(lista):
    if len(lista) <= 1:
        return lista

    pivote = lista[0]
    mayores = [x for x in lista[1:] if x[1]["paquetes_cantidad"] > pivote[1]["paquetes_cantidad"]]
    menores = [x for x in lista[1:] if x[1]["paquetes_cantidad"] < pivote[1]["paquetes_cantidad"]]

    return quick_sort(mayores) + [pivote] + quick_sort(menores)


def busqueda_de_valor(diccionario, objetivo):
    for elemento in diccionario:
        if elemento == objetivo:
            return diccionario[elemento]
    return None


mensajeria = {}
total_paquetes = 0
paquetes_cantidad = 0
print("===Registro de mensajeria ===")
cantidad = int(input("Ingrese la cantidad de repartidores que participaron: "))
for i in range(cantidad):
    print(f"Repartidor #{i + 1}")
    while True:
        mensajeria_nombre = input("Ingrese el nombre del repartidor: ")
        if mensajeria_nombre in mensajeria:
            print("Este nombre ya existe")
        else:
            break

    while True:
        try:
            paquetes_cantidad = int(input("Ingrese la cantidad de paquetes: "))
            if paquetes_cantidad <0:
                print("La cantidad debe de ser positiva")
            else:
                break
        except ValueError:
            print("Ingrese un numero valido")


    while True:
        zona = input("Ingrese la zona del repartidor: ")
        if zona == "":
            print("La zona no puede estar vacia")
        else:
            break
    mensajeria[mensajeria_nombre] = {
        "paquetes_cantidad": paquetes_cantidad,
        "zona": zona
    }
    total_paquetes = total_paquetes+paquetes_cantidad

print("=== Registro original ===")
for nombre, valor in mensajeria.items():
    print(f"Nombre: {nombre}, Valor: {valor['paquetes_cantidad']}, Zona {valor['zona']}")

print("=== Ranking ===")
repartidores = list(mensajeria.items())
resultado = quick_sort(repartidores)
for nombre, valor in resultado:
    print(f"nombre: {nombre}, paquetes: {valor['paquetes_cantidad']}, zona: {valor['zona']}")

print("=== Busqueda ===")
buscar_nombre = input("Ingrese el nombre: ")
resultadoA = busqueda_de_valor(mensajeria, buscar_nombre)
if resultadoA is not None:
        print(f"{buscar_nombre} entregó {resultadoA['paquetes_cantidad']} paquetes en la zona {resultadoA['zona']}.")
else:
    print("No se ha encontrado el resultado")

print("=== Estadisticas ===")
print(f"Total de paquetes entregados: {total_paquetes}")
promedio = total_paquetes/cantidad
print(f"Promedio de paquetes: {promedio:.2f}")