lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
        'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

multiploDe3 = 0

for elemento in lista:
    multiploDe3 += 2
    if multiploDe3 >= len(lista):
        break
    else:
        del lista[multiploDe3]

for elemento in lista:
    print(elemento)


