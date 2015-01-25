#!/usr/bin/env python

__author__ = 'wesleyreisz'

def main():
    get_input()

    return

def get_input():
    val = raw_input("input one: /> ")
    print(get_input_type(val))
    return

def get_input_type(val):
    if "one" == val:
        return "input is a string"
    else:
        return "input is a number"

main()