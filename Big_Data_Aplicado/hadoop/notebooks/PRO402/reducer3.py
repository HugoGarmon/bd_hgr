#!/usr/bin/env python3
 
import sys

ciudad = None
ciudad_actual = None
año_actual = None
lineafinal = ""
cont = 0

for line in sys.stdin:
    line = line.split(',',2)

    ciudad = line[0]
    temp = float(line[2])
    año = float(line[1])

    if ciudad_actual is None:
        ciudad_actual = ciudad

    if año_actual is None:
        año_actual = año
        
    if temp >= 30:
        cont += 1    

    
    if ciudad_actual != ciudad:
        cont = 0
        ciudad_actual = ciudad
    
    if año_actual != año:
        print(f"{año_actual}")
        lineafinal = f"Dias calurosos en  {ciudad_actual}  --->  {cont}"
        print(lineafinal)
        cont = 0
        año_actual = año
