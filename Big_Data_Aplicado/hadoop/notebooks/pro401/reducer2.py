#!/usr/bin/env python3

import sys

palabra_actual = None
cont = 0
dic = {}

for line in sys.stdin:
    palabra , val = line.strip().split("\t")
    val = int(val)

    if palabra in dic:
        dic[palabra] = dic[palabra] + 1
    else :
        dic[palabra] = val

for pal , val  in dic.items():
    print(f"{pal}, {val}")
