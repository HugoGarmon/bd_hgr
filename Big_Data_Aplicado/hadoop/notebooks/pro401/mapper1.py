#!/usr/bin/env python3

import sys
import string

simbolos = str.maketrans('',''  ,string.punctuation+'¿¡»«')

dic = {
    "á":"a",
    "ú":"u",
    "é":"e",
    "í":"i",
    "ó":"o"
}

acentos = str.maketrans(dic)

for line in sys.stdin:
    
    line = line.lower()

    line = line.translate(simbolos)
    line = line.translate(acentos)

    line = line.strip().split()
    for word in line:
        print(f"{word}\t1")
