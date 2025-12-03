#!/usr/bin/env python3

import sys
import string

simbolos = str.maketrans('','',string.punctuation+'¿¡»«')

dic = {
    "á":"a",
    "ú":"u",
    "é":"e",
    "í":"i",
    "ó":"o"
}

acentos = str.maketrans(dic)

dic2 = [
    "de",
    "la",
    "el",
    "y",
    "en",
    "que",
    "a",
    "los,"
    "del",
    "se",
]

for line in sys.stdin:
    
    line = line.lower()

    line = line.translate(simbolos)
    line = line.translate(acentos)
  
    line = line.strip().split()
    for word in line:
        if word not in dic2:
            print(f"{word}\t1")
        else:
            continue
