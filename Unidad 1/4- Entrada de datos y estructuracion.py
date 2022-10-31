cantidadAsignaturas = int(input("Ingrese la cantidad de materias del semestre: "))
diccionario = {}
i = 1

while cantidadAsignaturas > 0:
    cantidadAsignaturas -= 1
    nombreAsignatura = input("Ingrese el nombre de la materia N°" + str(i) + ": ")
    creditos = int(input("Ingrese la cantidad de creditos de la materia N°" + str(i) + ": "))
    diccionario.update({nombreAsignatura:creditos})
    
    i += 1


def imprimirCreditosTotales():
    totalCreditos = 0
    for a in diccionario:
        totalCreditos = totalCreditos + int(diccionario[a])
    print(diccionario)
    print("Los creditos totales son: " + str(totalCreditos))

imprimirCreditosTotales()






