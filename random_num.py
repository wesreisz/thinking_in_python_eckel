#!/usr/bin/env python

import random

def main() :
	print "Utility to Get Random List"
	myList = getList()
	print executeRandom(myList)
	return

def getList():
	myList = []
	print("Enter Teams (Leave Empty when done):")
	while True :
		myItem = str(raw_input(": /> "))
		if(len(myItem)<=0):
			break
		myList.append(myItem)
	return myList

def executeRandom(myList):
	random.shuffle(myList) # inplace shuffle
	return myList
	
main()