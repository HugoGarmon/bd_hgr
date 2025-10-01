# #Ejercicio 1

# dic = {"manzana" : 5 , "platano" : 3, "pera" : 2}

# input = input("Dime una fruta: ")
# if input in dic:
#     print("El precio de la fruta es: ", dic[input])
# else:  
#     print("La fruta no esta en el diccionario")

# #Ejercicio 2

# productos = {
#     "Electrónica": ["Smartphone", "Laptop", "Tablet", "Auriculares", "Smartwatch"],
#     "Hogar": ["Aspiradora", "Microondas", "Lámpara", "Sofá", "Cafetera"],
#     "Ropa": ["Camisa", "Pantalones", "Chaqueta", "Zapatos", "Bufanda"],
#     "Deportes": ["Pelota de fútbol", "Raqueta de tenis", "Bicicleta", "Pesas", "Cuerda de saltar"],
#     "Juguetes": ["Muñeca", "Bloques de construcción", "Peluche", "Rompecabezas", "Coche de juguete"],
# }

# sum = 0
# for categoria, items in productos.items():
#     print(f"{categoria}: {len(items)}")
#     sum += len(items)
# print(f"Total de productos: {sum}")


# # Ejercicio 3

# frase = "hola que tal, hola como va todo"
# contador = {}
# palabras = frase.split()
# for palabra in palabras:
#     if palabra in contador:
#         contador[palabra] += 1
#     else:
#         contador[palabra] = 1
# print(contador)


#Ejercicio 4

asignaturas = {
    "Matemáticas": ["Ana", "Carlos", "Luis", "María", "Jorge"],
    "Física": ["Elena", "Luis", "Juan", "Sofía"],
    "Programación": ["Ana", "Carlos", "Sofía", "Jorge", "Pedro"],
    "Historia": ["María", "Juan", "Elena", "Ana"],
    "Inglés": ["Carlos", "Sofía", "Jorge", "María"],
}

opc = 4
while opc > 3:
    print("Opciones:")
    print("1. Ver estudiantes por asignatura")
    print("2. Agregar estudiante a una asignatura")
    print("3. Eliminar estudiante de una asignatura")
    print("4. Salir")
    opc = int(input("Selecciona una opción: "))

    if opc == 1:
        asignatura = input("Dime la asignatura: ")
        if asignatura in asignaturas:
            print(f"Estudiantes en {asignatura}: {', '.join(asignaturas[asignatura])}")
        else:
            print("Asignatura no encontrada.")
    

