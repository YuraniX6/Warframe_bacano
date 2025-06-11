import os
os.system("cls")

print("-----------------Maquina de Bebidas-----------------------")
print("1.Coca-Cola-----------------------------------------------")
print("2.Inka-Cola-----------------------------------------------")
print("3.Fanta---------------------------------------------------")
print("4.Pepsi---------------------------------------------------")

try:
    bob = int(input("Ingrese la bebida deseada: "))
except:
    print("Usted no ha escojido una opcion")

if bob == 1:
    print("Escojio Coca-Cola")
elif bob == 2:
    print("Escojio Inka-Cola")
elif bob == 3:
    print("Escojio Fanta")
elif bob == 4:
    print("Escojio pepsi")
else: 
    print("Usted no ha escojido una bebida")
