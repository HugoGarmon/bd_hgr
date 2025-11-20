#!/usr/bin/env python3
 
import sys

max_temp = -100.0
ciudad = None
ciudad_actual = None
lineafinal = ""

for line in sys.stdin:
    line = line.split('\t',1)

    ciudad = line[0]
    temp = float(line[1])

    if ciudad_actual is None:
        ciudad_actual = ciudad
        
    if temp > max_temp:
        max_temp = temp
        lineafinal = f"{ciudad_actual}  --->  {temp}"

    if ciudad_actual != ciudad:
        print(lineafinal)
        ciudad_actual = ciudad
        max_temp = temp
