#!/usr/bin/env python3

import sys

grupo_actual = None
paises_set = set()

for line in sys.stdin:
    line = line.strip().split("\t")
        
    grupo = line[0]
    pais =  line[1]
    
    if grupo_actual == grupo:
        paises_set.add(pais)
    
    else:   
        if grupo_actual is not None:
            lista_paises = ", ".join(sorted(paises_set))
            print(f"{grupo_actual}\t{lista_paises}")
        
        grupo_actual = grupo
        paises_set = {pais}

if grupo_actual is not None:
    lista_paises = ", ".join(sorted(paises_set))
    print(f"{grupo_actual}\t{lista_paises}")
