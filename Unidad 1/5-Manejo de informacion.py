def imprimirInformacion(**nParametros):
    diccionario = {}
    for llave in nParametros:
       diccionario.update({llave:nParametros[llave]})
    print(diccionario)

imprimirInformacion(llave1 = 100, llave2 = 27, llave3 = 39, 
                    llave4 = 10, llave5 = 20, llave6 = 30)
