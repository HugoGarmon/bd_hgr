#!/usr/bin/env python3


import sys 

dic = {}

for line in sys.stdin:

    metodo , val = line.strip().split(",",1)
    val = int(val)

    if metodo not in dic:
        dic[metodo] = val  
    else: 
        dic[metodo] = dic[metodo] + val

for metodo , val in dic.items():
    print(f"{metodo} , {val}")
