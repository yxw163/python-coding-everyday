#! /usr/local/bin python3 
# -*- coding: utf-8 -*-
"""
	Description: 
		Write a function persistence, that takes a positive parameter num and 
		returns its mutltiplicative persistence, which is the number of times 
		you must multiply the digits num until you reach a single digit.

	For example:

 		persistence(39) => 3  # Because 3*9 = 27, 2*7 = 14, 1*4=4
                       # and 4 has only one digit.

 		persistence(999) => 4 # Because 9*9*9 = 729, 7*2*9 = 126,
                       # 1*2*6 = 12, and finally 1*2 = 2.

 		persistence(4) => 0   # Because 4 is already a one-digit number.

    Args:
        num (int)

    Author: 

    	yangxw163@gmail.com
        
    Created:

    	7 March 2017
"""
from functools import reduce
def persistence(n):
	i = 0
	while n >= 10:
		n = reduce(lambda x, y: int(x) * int(y), list(str(n)))
		i = i + 1
	return i

if __name__ == '__main__':
	print(persistence(25))