from os import system

def TaN(): #tiempo a numeros
    hora = [0,0,0] #reseteo en caso de que repitan
    print("\nA continuacion, ingresara horas, minutos y segundos.")
    hora[0] = int(input("Ingrese horas: "))
    #chequeo que no ingrese numeros negativos ni mayores a 60
    hora[1] = validar(0,60,"Ingresar minutos",2)
    hora[2] = validar(0,60,"Ingresar segundos",2)
    print(f"\nSu tiempo ingresado es {hora[0]}:{hora[1]}:{hora[2]}")
    #resolucion del ejercicio
    segundos = (hora[0]*3600) + (hora[1]*60) + hora[2]
    minutos = (hora[0]*60) + hora[1] + (hora[2]/60)
    horas  = hora[0] + (hora[1]/60) + (hora[2]/3600)
    round(minutos, 3)
    round(horas,3)
    print(f"Eso equivale a {segundos} segundos, {minutos} minutos y {horas} horas")
    #calculo en dias
    dias = segundos//86400
    diasH = (segundos - (dias*86400))//3600
    diasM = (segundos - (dias*86400)-(diasH*3600))//60
    diasS = segundos - (dias*86400)-(diasH*3600)-(diasM*60)
    #Cuestion sintactica
    if dias == 1:
        print(f"Eso es {dias} dia con {diasH}:{diasM}:{diasS}\n")
    else:
        print(f"Eso son {dias} dias con {diasH}:{diasM}:{diasS}\n")
#-----------------------------------------------------------------------------------
def NaT(): #numeros a tiempo
    rtaHora = [0,0,0] #reseteo en caso de que repitan
    ing = int(input("\nIngrese su tiempo en segundos: "))
    #calculo
    rtaHora[0] = ing//3600
    rtaHora[1] = (ing -(rtaHora[0]*3600))//60
    rtaHora[2] = ing - (rtaHora[0]*3600 + rtaHora[1]*60)
    print(f"El resultado: {rtaHora[0]}:{rtaHora[1]}:{rtaHora[2]}")
    #calculo dias
    dias = ing//86400
    diasH = (ing - (dias*86400))//3600
    diasM = (ing - (dias*86400)-(diasH*3600))//60
    diasS = ing - (dias*86400)-(diasH*3600)-(diasM*60)
    if dias == 1:
        print(f"Eso es {dias} dia con {diasH}:{diasM}:{diasS}\n")
    else:
        print(f"Eso son {dias} dias con {diasH}:{diasM}:{diasS}\n")
#-----------------------------------------------------------------------------------
def validar(c,g,txt,tipo):
    flag = 0
    if tipo == 1:
        while flag==0:
            x = int(input(f"{txt}: "))
            if x==c or x==g:
                flag = 1
        return x
    else:
        while flag==0:
            x = int(input(f"{txt}: "))
            if x>=c and x<g:
                flag = 1
        return x
#-----------------------------------------------------------------------------------
def main(): #uso un loop para usar las peticiones que gusten
    flag = 0
    while flag==0:
        op = validar(1,2,"Para transformar tiempo a numero ingresar 1, para ingresar un numero y recibir tiempo ingresar 2",1)
        if op == 1: 
            TaN()
        else:
            NaT()
        flag = validar(0,1,"Para terminar presione 1, para repetir presione 0\n",1)
        system("cls") #borro el contenido de la consola para que no se acumule
    print("Programa finalizado")
    system("pause")
#-----------------------------------------------------------------------------------
main()     