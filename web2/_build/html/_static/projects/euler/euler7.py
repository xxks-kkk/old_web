"""Solution to problem 7 in Project Euler

copyright (c) 2013, Zeyuan Hu, zhu45@wisc.edu
"""

__author__ = "Zeyuan Hu (zhu45@wisc.edu)"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2013/01/11 17:33:20 $"
__copyright_ = "Copyright (c) 2013 Zeyuan Hu"
__license__ = "Python"

from math import *
def isPrime(n):
	if n<= 1:
		return False
	i = 2.0
	while (i <= sqrt(n)):
		if n%i == 0:
			return False
		i += 1
	
	return True

def find(n):
	list = [2]
	i = 3
	count = 0
	while count < n-1:
		if isPrime(i):
			list.append(i)
			count += 1
		i += 2
	return list[count]
	
print "the 10 001st prime number is: %d"%find(10001)
