#!/usr/bin/env python3

import sys 

dic = {}

for line in sys.stdin:
    code , val = line.strip().split(" ",1)
    val = int(val)

    if code not in dic:
        dic[code] = val
    else:
        dic[code] = dic[code] + val


for code  ,val in dic.items():

    print(f"{code} , {val}")


