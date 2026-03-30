#!/usr/bin/python3
def uppercase(str):
    for char in str:
        temp_char = char
        if ord(char) >= 97 and ord(char) <= 122:
            temp_char = chr(ord(char) - 32)
        print("{}".format(temp_char), end="")
    print("")
