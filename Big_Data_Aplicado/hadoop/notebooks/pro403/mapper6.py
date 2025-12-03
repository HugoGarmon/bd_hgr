#!/usr/bin/env python3

import sys

for line in sys.stdin:

    line = line.strip().split()

    code = int(line[8])

    if code >= 400:
        print(f"{line[10]} , ({0}, {1})")
    else:
        print(f"{line[10]} , ({1}, {0})")

