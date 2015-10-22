"""Solution to problem 4 in Project Euler

copyright (c) 2013, Zeyuan Hu, zhu45@wisc.edu
"""

__author__ = "Zeyuan Hu (zhu45@wisc.edu)"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2013/01/11 03:10:05 $"
__copyright_ = "Copyright (c) 2013 Zeyuan Hu"
__license__ = "Python"

	
from math import *

# pure practice for the recursion data structure, nothing to do with the main program
def isPalindrome(num):

	if len(num) == 1 or len(num) == 0:
		return True
		
	first = num[0]
	last = num[len(num)-1]
	
	return (first == last) and isPalindrome(num[1:len(num)-1])

#print "is num %d a Palindrome? %s" % (9909,isPalindrome("9909"))

def find():
	list = []
	r = 0
	i = 999
	j = 999
	while j >= 100:
		while i >= 100:
			r = i*j
			#KEY: shortcut to reverse string
			if str(r) == str(r)[::-1]:
				list.append(r)
			i -= 1
		j -= 1
		i = j - 1
	list.sort()
	return list

print "largest Palindrome from product of the three-digit number is %s" % find()
