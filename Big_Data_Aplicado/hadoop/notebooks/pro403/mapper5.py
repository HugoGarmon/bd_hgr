#!/usr/bin/env python3

import sys

for line in sys.stdin:

    line = line.strip().split()

    fecha = line[3]

    hora = fecha[13:15]
    
   

    print(f"{hora}, 1")



    
