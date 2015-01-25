#!/usr/bin/env python

def main() :
	return
	
def getInput() :
	val = input("input one")
	return getInputType(val)
def getInputType(val):
	if "one"==val:
		return "input is a string"
	else:
		return "input is a numbers"	
	
main()