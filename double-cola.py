#! /usr/local/bin python3 
# -*- coding: utf-8 -*-
"""
	Description: 
		Sheldon, Leonard, Penny, Rajesh and Howard are in the queue 
		for a "Double Cola" drink vending machine; 
		there are no other people in the queue. 
		The first one in the queue (Sheldon) buys a can, 
		drinks it and doubles! 
		The resulting two Sheldons go to the end of the queue. 
		Then the next in the queue (Leonard) buys a can, 
		drinks it and gets to the end of the queue as two Leonards, and so on.

		For example, Penny drinks the third can of cola 
		and the queue will look like this:

		Rajesh, Howard, Sheldon, Sheldon, Leonard, Leonard, Penny, Penny

		Write a program that will return the name of a man 
		who will drink the n-th cola.

		Note that in the very beginning the queue looks like that:
		Sheldon, Leonard, Penny, Rajesh, Howard

	Output / Examples

		Return the single line — the name of the person 
		who drinks the n-th can of cola. 
		The cans are numbered starting from 1. 
		Please note that you should spell the names like this: 
		"Sheldon", "Leonard", "Penny", "Rajesh", "Howard" (without the quotes). 
		In that order precisely the friends are in the queue initially.

    Args:
        names: ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
        n: 1 ≤ n ≤ 1000000000

    Author: 

    	yangxw163@gmail.com
        
    Created:

    	26 Ferbary 2017
"""

def whoIsNext(names, r):
	while r > 5:
		r = int((r - 4) / 2)
	return names[r - 1]

if __name__ == '__main__':
	names = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]
	r = 1
	print(whoIsNext(names, 52))
