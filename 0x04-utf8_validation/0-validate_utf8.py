#!/usr/bin/python3
"""This module defines a function `validUTF8`"""


def validUTF8(data):
    """ Checks is all data within the list is a valid UTF8 encoding

        UTF8 Format:

        1-byte Sequence: 0xxxxxxx;
        2-byte Sequence: 110xxxxx 10xxxxxx;
        3-byte Sequence: 1110xxxx 10xxxxxx 10xxxxxx;
        4-byte Sequence: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx;
    """

    # 0x80 is 10000000
    # 0xE0 is 11100000
    # 0xC0 is 11000000
    # 0xF0 is 11110000

    i = 0
    while i < len(data):
        # Check if it's a single-byte character
        if data[i] & 0x80 == 0x00:
            i += 1
        # Check if it's a multi-byte character
        # 2-byte sequence
        elif data[i] & 0xE0 == 0xC0:
            # checks if there is a next term in the sequence and it is
            # of the format
            if i + 1 >= len(data) or data[i + 1] & 0xC0 != 0x80:
                return False
            i += 2
        # 3-byte sequence
        elif data[i] & 0xF0 == 0xE0:
            # checks if there are two other terms in the sequence and
            # they are of the format
            if i + 2 >= len(data) or data[i + 1] & 0xC0 != 0x80 or data[i + 2]\
                    & 0xC0 != 0x80:
                return False
            i += 3
        # 4-byte sequence
        elif data[i] & 0xF8 == 0xF0:
            # checks if there are three other terms in the sequence and
            # they are of the format
            if i + 3 >= len(data) or data[i + 1] & 0xC0 != 0x80 or data[i + 2]\
                    & 0xC0 != 0x80 or data[i + 3] & 0xC0 != 0x80:
                return False
            i += 4
        else:
            return False
    return True
