#!/usr/bin/env python3

import sys


dic = {}

for line in sys.stdin:
    genero , val = line.strip().split(",",1)
    generos = genero.strip().split(";")
    val = int(val)

    for genero in generos:
        
        if genero in dic:
            dic[genero] = dic[genero] + 1
        else :
            dic[genero] = val
for genero , val  in dic.items():
    print(f"{genero}, {val}")
