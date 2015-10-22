"""Solution to problem 6 in Project Euler

copyright (c) 2013, Zeyuan Hu, zhu45@wisc.edu
"""

__author__ = "Zeyuan Hu (zhu45@wisc.edu)"
__version__ = "$Revision: 0.1 $"
__date__ = "$Date: 2013/01/11 17:27:10 $"
__copyright_ = "Copyright (c) 2013 Zeyuan Hu"
__license__ = "Python"


from math import *

def diffSum(n):
	sum_square_n = n * (n+1) *(2*n+1) / 6.0
	sum_n_square = pow((1+n)*n / 2.0 , 2)
	return abs(sum_n_square - sum_square_n)

print diffSum(100)
