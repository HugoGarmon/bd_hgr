#!/usr/bin/env python3

import sys

for line in sys.stdin:

    val , resto = line.strip().split(" ",1)
    val = int(val)

    print(f"{val} {resto}")
