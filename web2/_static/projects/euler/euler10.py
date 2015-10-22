"""Solution to problem 10 in Project Euler

copyright (c) 2013, Zeyuan Hu, zhu45@wisc.edu
"""

__author__ = "Zeyuan Hu (zhu45@wisc.edu)"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2013/01/11 23:45:15 $"
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

# since we know that 2 and 3 are primes
summation = 5

for i in range(5,2000000):
    if isPrime(i):
        summation += i

print summation
