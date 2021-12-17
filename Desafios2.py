"""
Tenemos una lista donde se registran los ingresos delpersonal a un sistema:
personas =["Susana","Tamara","Ana","Susana","Susana","Tomas","Ana"]
Contar los ingresos en un diccionario. La clave deberíade ser el nombre y el valor debería ser la cantidad deingresos. 
"""

personas = ["Susana","Tamara","Ana","Susana","Susana","Tomas","Ana"]
login = {
    "Susana":0,
    "Tamara":0,
    "Ana":0,
    "Susana2":0,
    "Tomas":0,
    "Ana2":0
}
while True:
    user = input("Ingrese su nombre de usuario: ")
    user.capitalize
    for nombre in login:
        if nombre == user:
            login[user]+=1
            break

    