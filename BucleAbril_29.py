import os
os.system("cls")

print("Hola")
nombre = input("Ingresa tu nombre: ")
try:
    edad = int(input("Ingresa tu edad: "))
except:
    print ("Se esperaba un numero")

print(f"Bienvenido {nombre}, su edad es {edad}")
