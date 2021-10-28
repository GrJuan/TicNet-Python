from typing import List
import os
import time
import math
from math import asin,cos,sin,sqrt,radians,degrees
print('"Bienvenido al sistema de ubicación para zonas públicas WIFI"')
usuario = 51747
contraseña = "74715"
contraseñanueva = []
captcha1 = 747
captcha2 = (2+6)+(2+3)-9
captcha3 = captcha1 + captcha2
listacoor = []
ad1 = 4
ad2 = 7
instruccion = 6
op1 = "Cambiar contraseña"
op2 = "Ingresar coordenadas"
op3 = "Ubicar zona wifi más cercana"
op4 = "Guardar archivo con ubicación cercana"
op5 = "Actualizar registros de zonas wifi desde archivo"
op6 = "Elegir opción de menú favorita"
op7 = "Cerrar sesión"
lista_menu =[op1,op2,op3,op4,op5,op6,op7]
radiotierra = 6372.795477598
coorfija = [[2.698,-76.680,63],
            [2.724,-76.693,20],
            [2.606,-76.742,680],
            [2.698,-76.690,15]]
distancia = []
UbicacionActual = None
variabletiempo = None
wifiactual = []
listadistancias = []
archivoexp = []
archivo = "guardarinfo.txt"

def captcha():
    captcha = (int(input(f"cuanto es {captcha1} + {captcha2}:" )))
    if captcha == captcha3 :
        print("Sesión iniciada")
    else:
        print("Error")

def cambiarcontraseña(contraseñaactual):
    global contraseña
    contraseñanueva1 = input("Digite la contraseña actual: ")
    if contraseñanueva1 == contraseña:
        contraseñanueva = input("Digite contraseña nueva: ")
        if contraseñanueva == contraseñaactual:
           os.system("cls")
           print("Contraseña nueva no puede ser igual a la anterior")
           time.sleep(1)
           return contraseñaactual
        else:
            confirmarcontraseña = input("confirme su nueva contraseña: ")
            if confirmarcontraseña == contraseñanueva:
               os.system("cls")
               print("contraseña cambiada satisfactoriamente")
               time.sleep(1)
               os.system("cls")
               return contraseñanueva
            else:
                os.system("cls") 
                print("Las contraseñas no coinciden")
                time.sleep(1)
  
                return contraseñaactual
    else:
         os.system("cls")
         print("Error")
         time.sleep(1)
         exit()

def ingresarcoor(lista_original):
    lista_duplicada = list(lista_original)
    for x in range(0,3):
        lista_duplicada.append([])
        lat = float(input("Ingrese porfavor latitud: "))
        while lat == "" or lat == " ":
            lat = float(input("Ingrese nuevamente latitud: "))
        lat = float(lat)
        if lat<=2.766  and lat>=2.548:
            lon = float(input("Ingrese porfavor longitud: "))
            while lon == "" or lon == " ":
                lon = float(input("Ingrese nuevamente longitud: "))
                lon = float(lon)
            if lon>= -76.879 and lon<= -76.493:
                lista_duplicada[x].insert(0,lat)
                lista_duplicada[x].insert(1,lon)
            else:
                os.system
                print("Error coordenada")
                time.sleep(1)
                exit()
        else:
            os.system("cls")
            print("Error coordenada")
            time.sleep(1)
            exit()
    print("Coordenadas ingresadas correctamente")
    time.sleep(2)
    return lista_duplicada

def ordenarlatitudes(lista_original):
    print(f"coordenada ubicada más al oriente: {min(lista_original, key = lambda posicion: posicion[0])}")

def ordenarlongitudes(lista_original):
    print(f"coordenada ubicada más al occidente: {max(lista_original, key = lambda posicion: posicion[1])}")

def promediocoor(lista_original):
    print(f"Promedio de las latitudes es: {(lista_original[0][0])+(lista_original[1][0])+(lista_original[2][0])/3}")

def imprimircoor(lista_original):
    lista_duplicada = list(lista_original)
    print("las coordenadas actuales guardadas son: ")
    for x in range(0,len(lista_duplicada)):
        print(f"{x+1} lat:'{lista_duplicada[x][0]}' lon:'{lista_duplicada[x][1]}'")
    ordenarlatitudes(lista_duplicada)
    ordenarlongitudes(lista_duplicada)
    promediocoor(lista_duplicada)
    op=int(input("Presiones 1, 2 o 3 para actualizar la respectiva coordenada. presione 0 para regresar al menu: "))
    if op >= 4:
        os.system("cls")
        print("Error actualización")
        time.sleep(1)
        exit() 
    elif op == 0:
        menu()
    else:
        actualizarcoor(op,lista_original)

def actualizarcoor(op,lista_original):
    lista_duplicada = list(lista_original)
    op = op - 1
    lista_duplicada = list(lista_original)
    lat = float(input("Ingrese la latitud: "))
    while lat == "" or lat == " ":
        lat = float(input("Ingrese nuevamente latitud: "))
        lat = float(lat)
    if lat<=2.766  and lat>=2.548:
        lon = float(input("Ingrese porfavor longitud: "))
        while lon == "" or lon == " ":
            lon = float(input("Ingrese nuevamente longitud: "))
            lon = float(lon)
        if lon>= -76.879 and lon<= -76.493:
            lista_duplicada[op][0]=lat
            lista_duplicada[op][1]=lon
        else:
            os.system("cls")
            print("Error actualización")
            time.sleep(1)
            exit()  
    else:
        os.system("cls")
        print("Error actualización")
        time.sleep(1)
        exit()
    return(lista_duplicada)

def mostrarcoorfav(lista_original):
    if lista_original == []:
        os.system("cls")
        print("Error sin registro de coordenadas")
        time.sleep(1)
        exit()
    else:
        imprimircoorfav(lista_original)

def imprimircoorfav(lista_original):
    lista_duplicada = list(lista_original)
    print("las coordenadas actuales guardadas son: ")
    for x in range(0,len(lista_duplicada)):
        print(f"Coordenada [Latitud,Longitud] {x+1} : '[{lista_duplicada[x][0]} ]' '[{lista_duplicada[x][1]}]'")
    opc =int(input("Por favor elija su ubicación actual (1,2 ó 3) para calcular la distancia a los puntos de conexión: "))
    if opc == 1 or opc == 2 or opc ==3:
        #global wifiactual
        #wifiactual=listacoor[opc-1]
        global UbicacionActual
        UbicacionActual=listacoor[opc-1]
        os.system("cls")
        preparardistancia(opc,lista_duplicada,coorfija)
    else:
        os.system("cls")
        print("Error ubicación")
        time.sleep(1)
        exit()
 
def preparardistancia(ubicacion_actual,lista_original,coorseguras):
    lista_duplicada = list(lista_original)
    lista_duplicadafija = list(coorseguras)
    lat1 = lista_duplicada[ubicacion_actual-1][0]
    lon1 = lista_duplicada[ubicacion_actual-1][1]
    lat1 = convertir_rad(lat1)
    lon1 = convertir_rad(lon1)
    for x in range(0,len(lista_duplicadafija)):
        for y in range (0,2):
            lista_duplicadafija[x][y] = convertir_rad(lista_duplicadafija[x][y])
    apliformula_dis(lat1, lon1, lista_duplicadafija)

def convertir_rad(valor_convertir):
    return math.radians(valor_convertir)

def apliformula_dis(lat1, lon1, lista_radianes):
    for x in range(0,4):
        lat2 = lista_radianes[x][0]
        lon2 = lista_radianes[x][1]
        latdelta = lat2 - lat1
        londelta = lon2 - lon1
        calculo1 = math.sin(londelta/2)**2
        calculo1 = calculo1 * (math.cos(lat1)*math.cos(lat2))
        calculo1 = (math.sin(latdelta/2)**2)*calculo1
        calculo1 = math.sqrt(calculo1)
        calculo1 = math.asin(calculo1)
        calculo1 = (2*radiotierra)*calculo1
        calculo1 = round(calculo1*1000,2)
        distancia.append(calculo1)
    ordenar_dis(distancia)
    
def ordenar_dis(distancia):
    distancia_duplicada = list(distancia)
    min1=distancia_duplicada.index(min(distancia_duplicada))
    distancia_duplicada.pop(min1)
    min2=distancia.index(min(distancia_duplicada))

    coorcercanas(min1,min2,coorfija,distancia)

def coorcercanas(min1,min2,basededatos,listadistancias):
    for x in range (0,4):
        basededatos[x][0]=degrees(basededatos[x][0])
        basededatos[x][1]=degrees(basededatos[x][1])

    for x in range (0,len(coorfija)):
        if coorfija[min1][0]==coorfija[x][0] and coorfija[min1][1] == coorfija[x][1]:
            if coorfija[x][2]>coorfija[min1][2]:
                min1=coorfija.index(coorfija[x])

    global variabletiempo 
    if basededatos[min1][2] < basededatos[min2][2]:
        
        print("Zonas wifi cercanas con menos usuarios")
        print(f"La zona wifi 1: ubicada en '[{basededatos[min1][0]}','{basededatos[min1][1]}]' a {listadistancias[min1]} metros, tiene en promedio {basededatos[min1][2]} usuarios")
        print(f"La zona wifi 2: ubicada en '[{basededatos[min2][0]}','{basededatos[min2][1]}]' a {listadistancias[min2]} metros, tiene en promedio {basededatos[min2][2]} usuarios")
        opcdestino=int(input("Elija 1 o 2 Para recibir indicaciones de llegada: "))
        if opcdestino==1: 
            variabletiempo = listadistancias[min1] #asignamos la distancia final al valor elegido por el usuario
            indicaciones(UbicacionActual,basededatos[min1])
        elif opcdestino==2:
            variabletiempo = listadistancias[min2]
            indicaciones(UbicacionActual,basededatos[min2])
        else:
            os.system("cls")
            print("Error zona wifi")    
            time.sleep(1)
            exit()
    else:
        print("Zonas wifi cercanas con menos usuarios")
        print(f"La zona wifi 1: ubicada en '[{basededatos[min2][0]}','{basededatos[min2][1]}]' a {listadistancias[min2]} metros, tiene en promedio {basededatos[min2][2]} usuarios")
        print(f"La zona wifi 2: ubicada en '[{basededatos[min1][0]}','{basededatos[min1][1]}]' a {listadistancias[min1]} metros, tiene en promedio {basededatos[min1][2]} usuarios")
        opcdestino=int(input("Elija 1 o 2 para recibir indicaciones de llegada: "))
        if opcdestino==1:
            os.system("cls")
            variabletiempo = listadistancias[min2]
            indicaciones(UbicacionActual,basededatos[min2])
        elif opcdestino==2:
            os.system("cls")
            variabletiempo = listadistancias[min1]
            indicaciones(UbicacionActual,basededatos[min1])
        else:
            os.system("cls")
            print("Error zona wifi")    
            time.sleep(1)
            exit()

def indicaciones(ubiactual,ubidestino):
    latorigen = ubiactual[0]
    lonorigen = ubiactual[1]
    latdestino = ubidestino[0]
    londestino = ubidestino[1]

    if latorigen>latdestino:
        indi1 = "al sur"
    elif latorigen<latdestino:
        indi1 = "al norte"
    else:
        ""
    if lonorigen>londestino:
        indi2 = "al occidente"
    elif lonorigen<londestino:
        indi2 = "al oriente"
    else:
        ""
    if indi1 == "" and indi2 == "":
        print(f"Para llegar a la zona wifi dirigirse primero {indi2}")
    elif indi2 == "" and indi1 == "":
        print(f"Para llegar a la zona wifi dirigirse primero {indi1}")
    elif indi1 == "" and indi2 == "":
        print("Usted ya esta en el destino")
    else:
        print(f"Para llegar a la zona wifi dirigirse primero {indi1} y luego hacia {indi2}")

    calculartime()

def calculartime ():
    time1 = "segundos"
    time2 = "segundos"
    if variabletiempo == 0:
        print("")
    else:
        auto = variabletiempo/20.83
        pie = variabletiempo/0.483

        if auto > 60:
            auto = auto/60
            time1 = "minutos"

        if pie > 60:
            pie = pie/60
            time2 = "minutos"
        
        print(f"se tardara aproximadament {round(auto,2)} {time1} en auto y {round(pie,2)} {time2} a pie")
        opexit=(input("Presione 0 para salir: "))
        if opexit == 0:
            os.system("cls")
            print("hasta pronto")
            time.sleep(2)
            menu()

def mostrarexpor(lista_original):
    if lista_original == []:
        os.system("cls")
        print("Error de alistamiento")
        time.sleep(1)
        exit()
    else:
        exporArch(lista_original)

def exporArch(archivoexp):
    archivoexp = {"'actual'":UbicacionActual, "'zonawifi1'":coorfija[3],"'recorrido'":["auto",variabletiempo]}
    print(archivoexp)
    oparc = input("¿Está de acuerdo con la información a exportar? Presione 1 para confirmar 0 para regresar al menú principal: ")
    if oparc == "0":
         os.system("cls")
         print("hasta pronto")
         time.sleep(1)
         menu()   
    if oparc == "1":
        archivo = open(r'C:\Users\jessi\OneDrive\Escritorio\Mision tic 2022\Ciclo 1\Programacion\guardarinfo.txt',"w")
        archivo.write(str(archivoexp))
        print("Exportando archivo")
        time.sleep(1)
        exit()
    else:
        print("Exportando archivo")
        time.sleep(1)
        exit()   
    

def imporArch(archivo2):
        archivo2 = open(r'C:\Users\jessi\OneDrive\Escritorio\Mision tic 2022\Ciclo 1\Programacion\importar.txt',"a+",encoding="utf8")
        indice = 0
        for i in archivo2.readline():
            coorfija[indice] = i.strip().split(',')
            coorfija[indice][0] = float(coorfija[indice][0])
            coorfija[indice][1] = float(coorfija[indice][1])
            coorfija[indice][2] = int(coorfija[indice][2])
            indice +=1
        print("estas son las zonas wifi actualizadas")
        print(coorfija)
        while True:
            opcimp = input("“Datos de coordenadas para zonas wifi actualizados, presione 0 para regresar al menú principal: ")
            if opcimp == "0":
                os.system("cls")
                print("hasta pronto")
                time.sleep(1)
                menu()
def menu():
    global contraseña
    global listacoor
    global variabletiempo
    os.system ("cls")
    while True:
        for l in range(0,len(lista_menu)):
            print(f"{l+1} - {lista_menu[l]}")
        opcion = (int(input("Elija una opción :")))
        if opcion > 0 and opcion <= 7:
            opcion = lista_menu [opcion-1]
            if opcion == op1:
                print("Usted ha elegido la opción",opcion)
                contraseña=cambiarcontraseña(contraseña)
            elif opcion == op2:
                print("Usted ha elegido la opción",opcion)
                if listacoor == []:
                    listacoor = ingresarcoor(listacoor)
                else:
                    imprimircoor(listacoor)
            elif opcion == op3:
                print("Usted ha elegido la opción",opcion)
                mostrarcoorfav(listacoor)
            elif opcion == op4:
                print("Usted ha elegido la opción",opcion)
                mostrarexpor(listacoor)
            elif opcion == op5:
                print("Usted ha elegido la opción",opcion)
                imporArch(listacoor)
            elif opcion == op6:
                print("Usted ha elegido la opción",opcion)
                instruccion_usuario()
            elif opcion == op7:
                os.system("cls")
                print("Hasta pronto")
                exit()
            else:
                os.system("cls")
                print("Error")
                exit()
        else:
            os.system("cls")
            print("Error")
            exit()

def imprima_menu(lista_menu):
    numeral1 = 1
    for numeracion_menu in lista_menu:
        print(f'{numeral1}. {numeracion_menu}')
        numeral1+= 1

def instruccion_usuario():
    while True:
        try:
            item1 = (int(input('Seleccione opción favorita: ')))
            cambiar_m1 = item1 < len(lista_menu) and item1 < 6 and item1 > 0
            if cambiar_m1:
                lista_menu[item1- 1],lista_menu[0] = lista_menu[0], lista_menu[item1- 1]
                opcion_usuario()
                break
            else:
                print("Error")
                exit()
        except:
            exit()
def opcion_usuario():
    print("Responda las siguientes dos adivinanzas para continuar y guardar el cambio")
    adiv1 = int(input(f"Cuantas patas tiene un perro: "))
    adiv2 = int(input(f"Cuantos colores tiene el arcoiris: "))
    if adiv1 == ad1:
        if adiv2 == ad2:
            os.system("cls") 
            menu()
        else:
            print("Respuesta equivocada")
            opcion_usuario()
    else:
        print("Respuesta equivocada")
        opcion_usuario()

def login():
    usuario_usuario = (int(input("usuario:")))
    if usuario == usuario_usuario :
        contraseña_usuario = input("contraseña:")
        if contraseña == contraseña_usuario:
            captcha()
            os.system("cls")
            menu()
        else:
            print("Error")
            exit()
    else:
        print("Error")
        exit()
login()