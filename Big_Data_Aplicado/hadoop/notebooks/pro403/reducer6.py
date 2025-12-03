#!/usr/bin/env python3


import sys 

total = 0
sum = 0 

for line in sys.stdin:

    url , code = line.strip().split(",",1)
    code = code.strip()
    if code == "(1, 0)":
        sum = sum + 1
    total = total + 1


porcentaje = (sum / total) * 100

print(f"El porcentaje de errores es {porcentaje}%")
