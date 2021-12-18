"""
Dada 2 listas con números enteros, crear una tercera con los números que pertenecen a ambas. Pero con la salvedad que en esta tercera no debe tener elementos repetidos.
primera = [7, 5, 10, 9, 8, 1, 3, 5, 6, 3, 8, 0, 10, 9, 2]
segunda = [6, 9, 3, 7, 9, 10, 5, 10, 7, 4, 5, 3, 2, 10, 2]
Usar únicamente sentencias de control: condicionales y bucles. También es probable que tengas que usar el operador de pertenencia.
"""

primera = [7, 5, 10, 9, 8, 1, 3, 5, 6, 3, 8, 0, 10, 9, 2]
segunda = [6, 9, 3, 7, 9, 10, 5, 10, 7, 4, 5, 3, 2, 10, 2]
def buscar(lista, elem):
    pos = -1
    i=0
    for n in lista:
        if n == elem:
            pos = i
        else:
            i+=1
    return pos
def comparar(p,s):
    t = []
    for n in p:
        pos = buscar(s,n)
        if pos != -1:
            pos = buscar(t,n)
            if pos == -1:
                t.append(n)
    return t
def ordenar(t):
    desordenado = 1
    cota = len(t) - 1
    while desordenado!=0:
        desordenado=0
        for j in range(cota):
            if t[j]>t[j+1]:
                aux = t[j]
                t[j] = t[j+1]
                t[j+1] = aux
                desordenado = j
        cota = desordenado
tercera = comparar(primera,segunda)
ordenar(tercera)
print(tercera)