saludo = "Hola que tal"
print(saludo)

a = False   
if a: 
    print("Verdadero")    
else:
    print("Falso")  

print("Dime un numero: ")
num = int(input())
if(not num.isdigit()):
    print("No es un numero")
elif num % 2 == 0:
    print("Es par")
else:
    print("Es impar")   
