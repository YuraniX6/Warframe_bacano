import os
os.system("cls")

listado_usuarios = []


while True:
    os.system("cls")
    print("=== USUARIOS ===")
    print("1.- Ingresar usuario.")
    print("2.- Buscar usuario.")
    print("3.- Eliminar usuario.")
    print("4.- Salir.")
    try:
        opcion = int(input("Ingrese opción : "))
    except:
        input("Opcion no valida")

    if opcion == 1:
        nuevo_usuario = []

        os.system("cls") 
        print("1.- Ingresar usuario.")
        rut = input("Ingresa el RUT >")
        nombre = input("Ingresa el NOMBRE >")
        apellido = input("Ingresa el Apellido >")

        nuevo_usuario = [rut,nombre,apellido]

        listado_usuarios.append(nuevo_usuario)

        input("Usuario registrado")

    elif opcion == 2:
        print("2.- Buscar usuario.")
    elif opcion == 3:
        print("3.- Eliminar usuario.")
    elif opcion == 4:
        print("Salio del sistema")
        break
    else:
        input("Opcion no disponible, preione enter para continuar > ")
