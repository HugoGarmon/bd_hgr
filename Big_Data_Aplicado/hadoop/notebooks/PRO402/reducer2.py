#!/usr/bin/env python3
 
import sys

temp_acumulada = 0
media = 0
pais = None
pais_actual = None
lineafinal = ""
cont = 0

for line in sys.stdin:
    line = line.split('\t',1)

    pais = line[0]
    temp = float(line[1])

    if pais_actual is None:
        pais_actual = pais
        
    temp_acumulada += temp
    cont += 1

    if pais_actual != pais:
        media = temp_acumulada / cont
        lineafinal = f"{pais_actual}  --->  {round(media,2)}"
        cont = 0
        temp_acumulada = 0
        media = 0 
        pais_actual = pais
        print(lineafinal)
