#!/usr/bin/python3
# 2-print_alphabet.py
# Brennan D Baraban <375@holbertonschool.com>

"""program that prints the ASCII alphabet, in lowercase, not followed by a new line"""
for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
