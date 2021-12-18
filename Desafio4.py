#Hacer una función que calcule el promedio, si es posible, de todos los números primos que encuentre en una lista que se le pasa por argumento.
from os import system

def crearLista(cant):
    lista = [2]
    for n in range(cant - 1):
        if (n%2)!=0:
            lista.append(2+n)
    return lista
def transfPrimo(lista, cant):
    i=2
    while i<cant:
        for x in range(cant):
            aux = (2+x)**2
            if aux<cant:
                for elem in lista:
                    if elem == 2:
                        continue
                    else:
                        if (elem%(2+x)) == 0 and elem != (2+x):
                            borrar(lista,elem)
        i+=1
    print(lista)
def promedio(lista):
    aux = 0
    for x in lista:
        aux+=x 
    rta = aux/len(lista)
    print(f"El promedio de su lista es: {round(rta,2)}")
def borrar(lista, elem):
    for x in range(len(lista)):
        if lista[x] == elem:
            del(lista[x])
            break
def main():
    while True:
        nro = int(input("Todos los nros primos hasta el "))
        if nro >= 2:
            break
    lista = crearLista(nro)
    transfPrimo(lista,nro)
    promedio(lista) 
    system("pause")
main()