#!/usr/bin/python3
"""
a method that determined if a given data set
represents a valid utf-8 encoding
"""


def binary(dec):
    """the bits in an int"""
    remainders = []
    while True:
        if int(dec / 2) == 0:
            remainders.append(1)
            break

        remainders.append(int(dec % 2))
        dec = dec / 2

    string = ""
    for item in remainders[::-1]:
        string += str(item)

    if len(string) < 8:
        string = '0' + string

    return string


def validUTF8(data):
    """checking is data utf8 valid"""
    for item in data:
        msb = int(binary(item)[0])
        if msb != 0:
            return False

    return True
