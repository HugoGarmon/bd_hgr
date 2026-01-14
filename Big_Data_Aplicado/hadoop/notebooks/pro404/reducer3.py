#!/usr/bin/env python3

import sys 

pais_actual = None
maxVariacion = 0
año = 0

for line in sys.stdin:

    line = line.strip().split("\t")

    pais = line[0]
    yearVariation = line[1]

    yearVariation = yearVariation.strip().split(",")

    year = int(yearVariation[0])
    variation = float(yearVariation[1])

    if pais_actual == None:
        pais_actual = pais

    if pais_actual == pais: 
        if variation > maxVariacion:
            maxVariacion = variation
            año = year

    if pais_actual != pais:
        print(f"{pais_actual} \t {año} ({maxVariacion})")

        pais_actual = pais
        max_variacion = variation
        año_record = year
