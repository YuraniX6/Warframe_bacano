import os
os.system("cls")

edad = 0

while True:
    try:
        edad = int(input("Ingresa tu edad: "))
        break
    except:
        print ("Se esperaba un numero")

if edad == 0:
    print("Aun no nace")
elif edad > 0 and edad < 18:
    print("Es menor de edad")
elif edad >= 18 and edad < 65:
    print("Es mayor de edad")
elif edad >= 65 and edad <= 120:
    print("Es adulto mayor")
else:
    print("Usted es Extraterrestisimo")