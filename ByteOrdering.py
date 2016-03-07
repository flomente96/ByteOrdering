import numpy
import re

class ByteOrdering:
    temp = open("input.in", 'r').read().split('\n')
    print(temp)

    matrix_big = []
    matrix_little = []

    for input in temp:
        if input.isdigit() is False:
            while len(input) % 4 != 0:
                input += '0'
            t = re.findall('....', input)
            for s in t:
                matrix_big.append(s)
                matrix_little.append(s[::-1])
        else:
            i = 0
            t = ''
            while i < 3:
                t += '0'
                i += 1
            t += str(input)
            matrix_big.append(t)
            matrix_little.append(t)

    print("Big Endian")
    for string in matrix_big:
        print("[" + string + "]")
    print("\n")
    print("Little Endian")
    for string in matrix_little:
        print("[" + string + "]")
