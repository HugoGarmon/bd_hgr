# #Ejercicio 1

# num = input("Dime un numero: ")

# while not num.isdigit():
#     print("Dime un numero: ")
#     num = input()
# else:
#     print("Numero validado")


#Ejercicio 2

# n = int(input("Dime un numero: "))
# k = int(input("Dime otro numero: "))

# for i in range(1, k+1):
#     print(n," * ",i," = ",n * i)


#Ejercicio 3

# n = int(input("Dime la base del triangulo: "))

# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print("*", end="")
#     print("")

#Ejercicio 4

# n = int(input("Dime la base de la piramide: "))

# while n % 2 == 0:
#     print("Dime un numero impar: ")
#     n = int(input())

# for i in range(1, n+1):
#     print("")
#     for j in range(1, i+1):
#         print("*", end="")


#Ejercicio 5

# max = 0
# min = 0
# print("Dime 5 numeros: ")
# for i in range(5):
#     num = int(input())
#     if num > max:
#         max = num
#     if num < min:
#         min = num
# print("El numero maximo es: ", max," El minimo es: ", min)

#Ejercicio 6

# unidades = {"mm": 0.001, "cm": 0.01, "m": 1, "km": 1000}
# cantidad = float(input("Dime la cantidad: "))
# unidad_origen = input("Dime la unidad de origen (mm, cm, m, km): ")
# unidad_destino = input("Dime la unidad de destino (mm, cm, m, km): ")

# if unidad_origen in unidades and unidad_destino in unidades:
#     cantidad_metros = cantidad * unidades[unidad_origen]
#     cantidad_convertida = cantidad_metros / unidades[unidad_destino]
#     print(f"{cantidad} {unidad_origen} son {cantidad_convertida} {unidad_destino}")
# else:
#     print("Unidad no reconocida.")
    

#Ejercicio 7
import random

num = random.randint(1, 100)
intentos = 0
print("Adivina el numero entre 1 y 100: ")
while True:
    intento = int(input())
    intentos += 1
    if intento < num:
        print("Demasiado bajo. Intenta de nuevo.")
    elif intento > num:
        print("Demasiado alto. Intenta de nuevo.")
    else:
        print(f"Felicidades! Has adivinado el numero {num} en {intentos} intentos.")
        break

