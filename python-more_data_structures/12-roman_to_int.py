#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    rom_n = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    res = 0
    last_v = 0
    for char in reversed(roman_string):
        val = rom_n.get(char, 0)
        if val >= last_v:
            res += val
        else:
            res -= val
        last_v = val
    return res
