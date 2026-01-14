#!/usr/bin/env python3

pais_actual = None
presu_total = 0
bene_total = 0
cont = 0

import sys

for line in sys.stdin:
    pais , presu , bene   = line.strip().split(",",2)
    presu = float(presu)
    bene = float(bene)

    if pais_actual == None:
        pais_actual = pais
    
    if pais_actual != pais:
        rent = (bene_total - presu_total) / cont
        print(f"{pais_actual} , {round(rent,2)}")
        presu_total = 0
        bene_total = 0
        cont = 0
        pais_actual = pais
    
    if pais_actual == pais:
        presu_total = presu_total + presu
        bene_total = bene_total + bene
        cont = cont + 1
    
