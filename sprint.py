#● Elaborar un programa que recorra una lista con los nombres de 10 de sus futuros usuarios de tu
#aplicación (pueden ser personas, pacientes, organizaciones sociales o instituciones públicas).
#● Mediante una función, a todos los usuarios se les creará una cuenta automáticamente.
#● Asigne una contraseña para cada cuenta. La contraseña debe ser creada con random y debe
#cumplir con los siguientes criterios: mayúsculas, minúsculas y números.
#● Cada cuenta debe guardarse en una nueva variable con su respectiva contraseña.
#● Por cada cuenta debe pedir un número telefónico para contactarse.
#
#● El programa no terminará de preguntar por los números hasta que todas las organizaciones
#tengan un número de contacto asignado.
#● El programa debe verificar que el número telefónico tenga 8 dígitos numéricos.
#● Se debe guardar como un string.

import random
import string 
import time


#Lista de usuarios de la aplicación
usuarios = ["Awakemed", "Telovendo", "AwakeIT", "AwakeGames", "AwakeStore", "AwakeMusic", "Intravía", "AwakeBooks", "AwakeMovies", "AwakeFood", "AwakeTravel"]

#Diccionario de cuentas en el que se guardará el usuario, contraseña y número de contacto
cuentas = {}

#Función de normalización de entradas
def normaliza(entrada):
    resultado = ""
    for element in entrada:
        if element == "á":
            resultado = resultado + "a"
        elif element == "é":
            resultado = resultado + "e"
        elif element == "í":
            resultado = resultado + "i"
        elif element == "ó":
            resultado = resultado + "o"
        elif element == "ú":
            resultado = resultado + "u"
        else:
            resultado = resultado + element
    return resultado

#Función para crear nombres de usuarios, acepta un nombre y realiza normalizacion previa
def crea_usuario(entrada):
    nombre_usuario = normaliza(entrada.lower())
    return nombre_usuario

#Función para generar contraseña
def generar_pass(largo):
    caracteres = string.ascii_letters + string.digits
    contrasena = "".join(random.sample(caracteres, largo))
    return contrasena

#Función para validar número de contacto
def validar_numero(numero):
    if len(numero) == 8 and numero.isdigit():
        return True
    else:
        return False

#Función con ciclo para crear cuentas y pedir números de contacto 
def ciclo_usuarios():  
    for usuario in usuarios:
        contrasena = generar_pass(8)
        nombre_usario = crea_usuario(usuario)
        cuentas[usuario] = contrasena

        while True:
            num = input(f"Ingrese el número de contacto de {usuario}: ")
            if validar_numero(num):
                break
            else:
                print("Número inválido. Debe tener 8 dígitos numéricos.")
        cuentas[usuario] = {"nombre_usuario": nombre_usario,"contraseña": contrasena, "celular": str(num)}

#Función para imprimir cuentas creadas
def resultado_usuarios():
    print("\nCuentas creadas:")
    for usuario, datos in cuentas.items():
        print(f"Organización: {usuario} - Nombre de usuario: {datos['nombre_usuario']} - Contraseña asignada: {datos['contraseña']} - Celular: {datos['celular']}")
        time.sleep(2)

ciclo_usuarios()
resultado_usuarios()