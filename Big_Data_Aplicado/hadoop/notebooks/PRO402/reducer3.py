#!/usr/bin/env python3
 
import sys

ciudad = None
ciudad_actual = None
lineafinal = ""
cont = 0

for line in sys.stdin:
    line = line.split('\t',1)

    pais = line[0]
    temp = float(line[1])

    if ciudad_actual is None:
        ciudad_actual = ciudad
        
    if temp >= 30:
        cont += 1    

    if ciudad_actual != ciudad:
        lineafinal = f" {ciudad_actual}  --->  {cont}"
        cont = 0
        ciudad_actual = ciudad
        print(lineafinal)
