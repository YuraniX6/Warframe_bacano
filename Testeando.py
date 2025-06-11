import os

os.system("cls")

cantidad_esquema_completo = 0
cantidad_esquema_incompleto = 0


while True:
    try:
        cantidad_elemento = int(input("Ingrese la cantidad de personas a registrarse: "))
        if cantidad_elemento <= 0:
            input("Debe ingresar un numero entero")
        else:
            break
    except:
        input("opcion no valida")

for i in range(1,cantidad_elemento):
    while True:
        try:
            cantidad_dosis_recibidas = int(input("Ingrese cantidad de dosis recibidas: "))
            if cantidad_dosis_recibidas <= 0 and cantidad_dosis_recibidas > 3:
                input("La cantidad de dosis no debe ser mayor a 3")
            else:
                if cantidad_dosis_recibidas >= 3:
                    cantidad_esquema_completo += 1
                    print("Esquema completo")
                else:
                    cantidad_esquema_incompleto += 1
                    print("Esquema incompleto")
                    break

        except:
            input("opcion no valida")

print(f"Se registraron {cantidad_esquema_completo} personas con esquema completo")
print(f"Se registraron {cantidad_esquema_incompleto} personas con esquema incompleto")
