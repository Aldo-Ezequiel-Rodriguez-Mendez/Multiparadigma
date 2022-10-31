nombre = input("Ingrese su nombre: ")
lista = []
lista = list(nombre)

def imprimirNombreInverso():
    longitudArreglo = len(lista)
    while longitudArreglo > 0:
        longitudArreglo -= 1
        print(lista[longitudArreglo])

imprimirNombreInverso()