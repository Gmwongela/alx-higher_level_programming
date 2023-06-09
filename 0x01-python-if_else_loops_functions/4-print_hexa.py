#!/usr/bin/python3
# 4-print_hexa.py
# Brennan D Baraban <375@holbertonschool.com>

"""Programme that print numbers 0 to 98 in decimal and hexadecimal"""
for number in range(0, 99):
    print("{} = {}".format(number, hex(number)))
