#!/usr/bin/env python3


import sys 

dic = {}

for line in sys.stdin:

    url , val = line.strip().split(",",1)
    val = int(val)

    if url not in dic:
        dic[url] = val  
    else: 
        dic[url] = dic[url] + val

for url , val in dic.items():
    print(f"{url} , {val}")
