#! /usr/local/bin python3
# -*- coding: utf-8 -*-
"""
	Description:
		At a job interview, you are challenged to write an algorithm
		to check if a given string, s, can be formed from two other strings,
		part1 and part2.

		The restriction is that the characters in part1 and part2
		are in the same order as in s.

		The interviewer gives you the following example and tells
		you to figure out the rest from the given test cases.

	Example:

		'codewars' is a merge from 'cdw' and 'oears':

    	s:  c o d e w a r s   = codewars
		part1:  c   d   w         = cdw
		part2:    o   e   a r s   = oears

    Args:
        s (string), part1 (string), part2 (string)

    Author:

    	yangxw163@gmail.com

    Created:

    	27 Ferbary 2017
"""


def is_merge(s, part1, part2):
	if not part1:
		return s == part2
	if not part2:
		return s == part1
	if not s:
		return part1 + part2 == ''

	if s[0] == part1[0] and is_merge(s[1:], part1[1:], part2):
		return True

	if s[0] == part2[0] and is_merge(s[1:], part1, part2[1:]):
		return True

if __name__ == '__main__':
	print(is_merge('Bananas', 'Bahamas', ''))
	
