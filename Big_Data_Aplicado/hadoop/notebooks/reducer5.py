#!/usr/bin/env python3


import sys 

dic = {}

for line in sys.stdin:

    hora , val = line.strip().split(",",1)
    val = int(val)


    if hora not in dic:
        dic[hora] = val  
    else: 
        dic[hora] = dic[hora] + val

for hora , val in dic.items():
    print(f"{hora} , {val}")
