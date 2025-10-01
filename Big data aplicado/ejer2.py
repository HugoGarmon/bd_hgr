#Ejercicio 1

# def contar_vocales_consonantes(cadena):
#     vocales = "aeiouAEIOU"
#     num_vocales = 0
#     num_consonantes = 0

#     for char in cadena:
#         if char.isalpha():              
#             if char in vocales:
#                 num_vocales += 1
#             else:
#                 num_consonantes += 1

#     return num_vocales, num_consonantes

# cad = "Hola Mundo"
# print(contar_vocales_consonantes(cad))

# #Ejercicio 2

# cad = "Hola Mundo"
# print(cad[::-1])

# #Ejercicio 3
# cad = "Hola Mundo"

# if cad == cad[::-1]:
#     print("Es un palíndromo")
# else:
#     print("No es un palíndromo")

#Ejercicio 4 

# cad = "Hola Mundo Mundo Mundo"
# cad = cad.split()
# print(len(cad))


#Ejercicio 5
#Eliminar caracteres duplicados en una cadena
# cad = "programacion"
# duplicados = ""
# for char in cad:
#     if char not in duplicados:
#         duplicados += char

# print(duplicados)

#Ejercicio 6
# cad = "Hola Mundo"

# for char in cad:
#     if char.isupper():
#         char = char.lower()
#     elif char.islower():
#         char = char.upper()
#     else:
#         char = char
#     print(char, end="")


#Ejercicio 7
# cad = "Hola Mundo"
# cad = cad.split()

# for i in range(len(cad)):
#     cad[i] = cad[i::-1]
# print(cad)


#Ejercicio 8
# cad = "roma"
# anagramas = ["amor", "ramo","hola"]
# resultado = []
# for palabra in anagramas:
#     if sorted(cad) == sorted(palabra):
#         resultado.append(palabra)

# print(resultado)

#Ejercicio 9

#Crea una función que reciba una cadena y devuelva un diccionario con la frecuencia de cada carácter.

# cad = "Hola Mundo"
# frecuencia = {}
# for char in cad:
#     if char in frecuencia:
#         frecuencia[char] += 1
#     else:
#         frecuencia[char] = 1
# print(frecuencia)

#Ejercicio 10


# cad = "Hola, Mundo! ¿Cómo estás?"
# resultado = ""
# for char in cad:
#     if char.isalnum() or char.isspace():
#         resultado += char
# print(resultado)


#Ejercicio 11
# cad = "hola mundo como estas"
# palabras = cad.split()
# for i in range(1, len(palabras)):
#     palabras[i] = palabras[i].capitalize()
# print("".join(palabras))

#Ejercicio 12
#Codificación RLE (Run-Length Enconding)

# cad = "aaabbbccdaa"
# resultado = ""
# i = 0
# while i < len(cad):
#     count = 1
#     while i + 1 < len(cad) and cad[i] == cad[i + 1]:
#         count += 1
#         i += 1
#     resultado += cad[i] + str(count)
#     i += 1
# print(resultado)

#Ejercicio 13
# Decodificar RLE
# cad = "a3b3c2d1a2"
# resultado = ""
# i = 0
# while i < len(cad):
#     char = cad[i]
#     i += 1
#     count = ""
#     while i < len(cad) and cad[i].isdigit():
#         count += cad[i]
#         i += 1
#     resultado += char * int(count)
# print(resultado)

#Ejercicio 14 


# #Ejercicio 15
# cad1 = "Hola Mundo"
# cad2 = "Hola Mundo que tal va todo"

# v1 = 0
# v2 = 0
# cad1 = list(cad1)
# cad2 = list(cad2)
# for i in range(len(cad1)):
#     valor = ord(cad1[i])
#     v1 += valor
# for j in range(len(cad2)):
#     valor = ord(cad2[j])
#     v2 += valor
    
# if v1 > v2:
#     cad1 = "".join(cad1)
#     print(cad1)
# else:
#     cad2 = "".join(cad2)
#     print(cad2)

#Ejercicio 16
# cad = "Hola Mundo"
# cad = cad.split()

# max_len = 0
# palabra_mas_larga = ""
# for palabra in cad:
#     if len(palabra) > max_len:
#         max_len = len(palabra)
#         palabra_mas_larga = palabra
# print(palabra_mas_larga)

#Ejercicio 17
# cad = "123456789"
# caracteres = list(cad)
# for i in range(len(caracteres)):
#     if (i+1) % 3 == 0 and i != len(caracteres) - 1:
#         caracteres[i] = caracteres[i] + "."
    
# cad = "".join(caracteres)
# print(cad)

#Ejercicio 18
# cad = "abcdefgh" 

# n = int(input("Cuantas veces quieres rotar la cadena"))
# for i in range(n):
#     cad = cad[-1] + cad[:-1]
# print(cad)


#Ejercicio 19
# cad = "Hola mundo    python  "
# cad = list(cad)
