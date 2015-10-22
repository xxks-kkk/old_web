"""Solution to problem 3 in Project Euler

copyright (c) 2013, Zeyuan Hu, zhu45@wisc.edu
"""

__author__ = "Zeyuan Hu (zhu45@wisc.edu)"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2013/01/11 15:05:30 $"
__copyright_ = "Copyright (c) 2013 Zeyuan Hu"
__license__ = "Python"


from math import *

#KEY: there cannot be a number greater than the square root of that number being prime
def isPrime(n):
	if n<= 1:
		return False
	i = 2.0
	while (i <= sqrt(n)):
		if n%i == 0:
			return False
		i += 1
	
	return True


def factor(n):
	i = 2
	list = []
	while(i<sqrt(n)):
		if isPrime(i) and (n%i == 0):
			list.append(i)
		i += 1
	return list[len(list)-1]
	

print factor(600851475143)
#print "Is %d a prime number? %s" % (5,isPrime(5))
