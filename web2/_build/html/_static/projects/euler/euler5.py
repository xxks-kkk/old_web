#!/usr/bin/env python
"""Solution to problem 5 in Project Euler

copyright (c) 2013, Zeyuan Hu, zhu45@wisc.edu
"""

__author__ = "Zeyuan Hu (zhu45@wisc.edu)"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2013/01/11 03:12:10 $"
__copyright_ = "Copyright (c) 2013 Zeyuan Hu"
__license__ = "Python"

from math import *
import numpy as np

def isPrime(n):
	if n<= 1:
		return False
	i = 2.0
	while (i <= sqrt(n)):
		if n%i == 0:
			return False
		i += 1
	
	return True
	
def minDivisible(k):
	# N: the value the function is going to return
	N = 1
	# index number
	i = 0
	check = True
	# upper bound of the estimation process for a[i]
	limit = sqrt(k)
	a = np.zeros(20)
	# plist is the prime list
	plist = []
	j = 1
	while j <= k:
		if isPrime(j):
			plist.append(j)
		j += 1
		
	while i < len(plist):
		#print "index of the list before increment:%d"%i
		a[i] = 1
		if check:
			if plist[i] <= limit:
				a[i] = int( log10(k) / log10(plist[i]) )
			else:
				check = False
		#print "N: %d"%N
		N = N * plist[i]**a[i]
		i = i + 1
		#print "index of the list after increment:%d"%i
	
	#print a
	return N

print"the smallest number divisible by each of the numbers 1 to 20 is: %d" % minDivisible(20)		
