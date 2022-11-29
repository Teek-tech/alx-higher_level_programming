#!/usr/bin/python3

lwup = 0
for n in range(122, 96, -1):
    if n % 2 == 0:
        lwup = n
    else:
        lwup = n - 32
    print('{}'.format(chr(lwup)), end='')
