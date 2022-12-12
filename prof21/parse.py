#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print("USAGE: ./parse.py <binary number> [-u | -s | -f]")
    print("     -u parse as unsinged int")
    print("     -s parse as signed int")
    print("     -f parse as 32-bit floating point")
    exit(1)

num = sys.argv[1]

for bit in num:
    try:
        assert bit == '0' or bit == '1'
    except AssertionError:
        print(f"ERROR: couldn't parse {num} as binary number")
        exit(1)


if sys.argv[2] == '-u':
    total = 0
    for i, bit in enumerate(num[::-1]):
        total += 2**(i)*int(bit)
    print("unsigned:")
    print(total)
    exit(0)

if sys.argv[2] == '-s':
    total = -2**(len(num)-1)*int(num[0])
    for i, bit in enumerate(num[:0:-1]):
        total += 2**(i)*int(bit)
    print("signed:")
    print(total)
    exit(0)

if sys.argv[2] == '-f':
    s = 1
    k = 8
    n = 23

    print("floating point:")
    
    assert len(num) == 32, "please provide 32 bit binary string"

    
    BIAS = 2**(k-1) - 1
    e = num[s:s+k]
    f = num[k+1:]
    s = num[:s]
    print("e=",e)
    print("f=",f)
    print("s=",s)

    #denormalized
    if int('0b' + e, 2) == 0:
        E = 1 - BIAS
        M = int('0b' + f, 2) / (2**n)
        print((-1)**int(s) * M * 2**E)
        exit(0)
    if e == '11111111':
        if int('0b' + f, 2) == 0:
            if s == '0':
                print("inf")
                exit(0)
            else:
                print("-inf")
                exit(0)
        else:
            print("NaN")
            exit(0)
    else:
        E = int('0b' + e, 2) - BIAS
        M = int('0b' + f, 2) / (2**n)+1
        print((-1)**int(s) * M * 2**E)
        exit(0)
