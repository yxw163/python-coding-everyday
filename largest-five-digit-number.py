#! /usr/local/bin python3 
# -*- coding: utf-8 -*-
"""
	Description: 
		In the following 6 digit number:
		283910
		91 is the greatest sequence of 2 digits.
		Complete the solution so that it returns 
		the largest five digit number found within the number given.
		The number will be passed in as a string of only digits. 
		It should return a five digit integer. 
		The number passed may be as large as 1000 digits.

    Args:
        digits (str)

    Author: 

    	yangxw163@gmail.com
        
    Created:

    	25 Ferbary 2017
"""
def solutions(digits):
	front = digits[0]
	result = 0
	for step in range(1, len(digits) - 4):
		if front < digits[step]:
			front = digits[step]
			result = step
		elif front == digits[step]:
			if digits[result:result + 5] < digits[step: step + 5]:
				result = step
			else:
				pass
		else:
			pass
		print (step)
	return digits[result: result + 5]

#优雅的实现
def solutions(digits):
	return max( int(digits[i:i+5]) for i in range(0, len(digits) - 4))


if __name__ == '__main__':
	s = '7316717653133062491922511967442657474235534919493496983520368542506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753123457977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257540920752963450'
	s1 = '1234567898765'
	print(solutions(s))
	
